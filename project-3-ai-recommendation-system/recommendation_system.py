# DecodeLabs Artificial Intelligence Internship
# Project 3: AI Recommendation Logic
#
# Advanced Content-Based Course Recommendation System
#
# Features:
# - Loads course data from CSV
# - Accepts user interests
# - Supports keyword aliases such as ML and AI
# - Uses TF-IDF vectorization
# - Uses cosine similarity
# - Ranks the top recommendations
# - Displays similarity percentages
# - Explains why each recommendation was selected
# - Allows repeated recommendation sessions
# - Saves recommendation results as CSV
# - Saves a recommendation-score visualization
# - Collects optional user feedback

import csv
from pathlib import Path

import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# --------------------------------------------------
# 1. Define paths
# --------------------------------------------------

PROJECT_FOLDER = Path(__file__).parent
COURSES_FILE = PROJECT_FOLDER / "courses.csv"
OUTPUT_FOLDER = PROJECT_FOLDER / "generated-output"

OUTPUT_FOLDER.mkdir(exist_ok=True)

RECOMMENDATIONS_FILE = OUTPUT_FOLDER / "recommendations.csv"
FEEDBACK_FILE = OUTPUT_FOLDER / "feedback.csv"
CHART_FILE = OUTPUT_FOLDER / "recommendation_scores.png"


# --------------------------------------------------
# 2. Keyword aliases
# --------------------------------------------------

ALIASES = {
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "dl": "deep learning",
    "nlp": "natural language processing",
    "web": "web development",
    "frontend": "frontend development",
    "backend": "backend development",
    "db": "databases",
    "sql": "databases sql",
    "cloud computing": "cloud",
    "cyber": "cybersecurity",
    "github": "git github version control",
    "flutter": "flutter dart mobile development",
    "oop": "object oriented programming"
}


# --------------------------------------------------
# 3. Load courses from CSV
# --------------------------------------------------

def load_courses(file_path):
    courses = []

    with open(file_path, mode="r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            combined_text = (
                f"{row['title']} "
                f"{row['description']} "
                f"{row['tags']} "
                f"{row['level']}"
            ).lower()

            course = {
                "course_id": row["course_id"],
                "title": row["title"],
                "description": row["description"],
                "tags": row["tags"],
                "level": row["level"],
                "combined_text": combined_text
            }

            courses.append(course)

    return courses


# --------------------------------------------------
# 4. Clean and expand user interests
# --------------------------------------------------

def clean_and_expand_interests(user_input):
    raw_interests = user_input.split(",")
    cleaned_interests = []
    expanded_interests = []

    for interest in raw_interests:
        cleaned_interest = interest.strip().lower()

        if not cleaned_interest:
            continue

        cleaned_interests.append(cleaned_interest)

        if cleaned_interest in ALIASES:
            expanded_interests.append(ALIASES[cleaned_interest])
        else:
            expanded_interests.append(cleaned_interest)

    expanded_query = " ".join(expanded_interests)

    return cleaned_interests, expanded_query


# --------------------------------------------------
# 5. Generate recommendations using TF-IDF
#    and cosine similarity
# --------------------------------------------------

def generate_recommendations(courses, user_query, top_n=5):
    course_documents = [
        course["combined_text"]
        for course in courses
    ]

    documents = course_documents + [user_query]

    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf_matrix = vectorizer.fit_transform(documents)

    course_vectors = tfidf_matrix[:-1]
    user_vector = tfidf_matrix[-1]

    similarity_scores = cosine_similarity(
        user_vector,
        course_vectors
    ).flatten()

    recommendations = []

    for course, similarity_score in zip(courses, similarity_scores):
        if similarity_score > 0:
            recommendation = {
                "course_id": course["course_id"],
                "title": course["title"],
                "description": course["description"],
                "tags": course["tags"],
                "level": course["level"],
                "similarity_score": similarity_score,
                "similarity_percentage": similarity_score * 100
            }

            recommendations.append(recommendation)

    recommendations.sort(
        key=lambda recommendation: recommendation["similarity_score"],
        reverse=True
    )

    return recommendations[:top_n]


# --------------------------------------------------
# 6. Explain recommendations
# --------------------------------------------------

def create_explanation(recommendation, user_interests):
    matching_words = []

    searchable_text = (
        f"{recommendation['title']} "
        f"{recommendation['description']} "
        f"{recommendation['tags']}"
    ).lower()

    for interest in user_interests:
        expanded_interest = ALIASES.get(interest, interest)

        individual_words = expanded_interest.split()

        for word in individual_words:
            if word in searchable_text and word not in matching_words:
                matching_words.append(word)

    if matching_words:
        return (
            "Recommended because it aligns with: "
            + ", ".join(matching_words)
        )

    return "Recommended based on overall content similarity."


# --------------------------------------------------
# 7. Display recommendations
# --------------------------------------------------

def display_recommendations(recommendations, user_interests):
    print("\nTop Recommended Courses")
    print("=" * 70)

    if not recommendations:
        print("No relevant recommendations were found.")
        print("Try interests such as python, ai, cloud, web, or automation.")
        return

    for index, recommendation in enumerate(recommendations, start=1):
        explanation = create_explanation(
            recommendation,
            user_interests
        )

        print(f"{index}. {recommendation['title']}")
        print(f"   Level: {recommendation['level']}")
        print(
            "   Similarity Score: "
            f"{recommendation['similarity_percentage']:.2f}%"
        )
        print(f"   Description: {recommendation['description']}")
        print(f"   Why recommended: {explanation}")
        print("-" * 70)


# --------------------------------------------------
# 8. Save recommendations to CSV
# --------------------------------------------------

def save_recommendations(recommendations, user_interests):
    with open(
        RECOMMENDATIONS_FILE,
        mode="w",
        newline="",
        encoding="utf-8-sig"
    ) as file:
        fieldnames = [
            "rank",
            "user_interests",
            "course_id",
            "title",
            "level",
            "similarity_percentage",
            "description"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for index, recommendation in enumerate(
            recommendations,
            start=1
        ):
            writer.writerow(
                {
                    "rank": index,
                    "user_interests": ", ".join(user_interests),
                    "course_id": recommendation["course_id"],
                    "title": recommendation["title"],
                    "level": recommendation["level"],
                    "similarity_percentage": (
                        f"{recommendation['similarity_percentage']:.2f}"
                    ),
                    "description": recommendation["description"]
                }
            )

    print(f"\nRecommendations saved to:\n{RECOMMENDATIONS_FILE}")


# --------------------------------------------------
# 9. Save visualization chart
# --------------------------------------------------

def save_recommendation_chart(recommendations):
    if not recommendations:
        return

    titles = [
        recommendation["title"]
        for recommendation in recommendations
    ]

    scores = [
        recommendation["similarity_percentage"]
        for recommendation in recommendations
    ]

    plt.figure(figsize=(10, 6))
    plt.barh(titles, scores)
    plt.xlabel("Similarity Score (%)")
    plt.ylabel("Course")
    plt.title("Top Course Recommendation Scores")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(CHART_FILE)
    plt.close()

    print(f"\nVisualization saved to:\n{CHART_FILE}")


# --------------------------------------------------
# 10. Collect optional feedback
# --------------------------------------------------

def collect_feedback(recommendations):
    if not recommendations:
        return

    print("\nOptional Feedback")
    print("-" * 70)

    rating_input = input(
        "Rate the recommendations from 1 to 5, "
        "or press Enter to skip: "
    ).strip()

    if not rating_input:
        print("Feedback skipped.")
        return

    if rating_input not in ["1", "2", "3", "4", "5"]:
        print("Invalid rating. Feedback was not saved.")
        return

    file_exists = FEEDBACK_FILE.exists()

    with open(
        FEEDBACK_FILE,
        mode="a",
        newline="",
        encoding="utf-8-sig"
    ) as file:
        fieldnames = [
            "rating",
            "top_recommendation"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(
            {
                "rating": rating_input,
                "top_recommendation": recommendations[0]["title"]
            }
        )

    print("Feedback saved successfully.")


# --------------------------------------------------
# 11. Display available commands
# --------------------------------------------------

def display_help():
    print("\nAvailable Commands")
    print("=" * 70)
    print("recommend     Start a new recommendation session")
    print("courses       Display all available courses")
    print("help          Display available commands")
    print("exit          Close the recommendation system")
    print("=" * 70)


# --------------------------------------------------
# 12. Display all available courses
# --------------------------------------------------

def display_courses(courses):
    print("\nAvailable Courses")
    print("=" * 70)

    for course in courses:
        print(
            f"{course['course_id']}. "
            f"{course['title']} "
            f"({course['level']})"
        )

    print("=" * 70)


# --------------------------------------------------
# 13. Run one recommendation session
# --------------------------------------------------

def run_recommendation_session(courses):
    print("\nEnter your interests separated by commas.")
    print("Example: python, ai, automation")
    print("Aliases such as ml, ai, nlp, web, and cyber are supported.")
    print("-" * 70)

    user_input = input("Your interests: ")

    user_interests, expanded_query = clean_and_expand_interests(
        user_input
    )

    if not user_interests:
        print("No interests were entered.")
        return

    recommendations = generate_recommendations(
        courses,
        expanded_query,
        top_n=5
    )

    display_recommendations(
        recommendations,
        user_interests
    )

    save_recommendations(
        recommendations,
        user_interests
    )

    save_recommendation_chart(
        recommendations
    )

    collect_feedback(
        recommendations
    )


# --------------------------------------------------
# 14. Main program loop
# --------------------------------------------------

def main():
    print("DecodeLabs Advanced AI Course Recommendation System")
    print("=" * 70)

    courses = load_courses(COURSES_FILE)

    print(f"Loaded {len(courses)} courses successfully.")
    print("Type 'help' to view the available commands.")
    print("Type 'recommend' to start.")
    print("Type 'exit' to close the program.")

    while True:
        print("-" * 70)

        command = input("Command: ").strip().lower()

        if command == "recommend":
            run_recommendation_session(courses)

        elif command == "courses":
            display_courses(courses)

        elif command == "help":
            display_help()

        elif command in ["exit", "quit", "bye"]:
            print("Recommendation system closed. Goodbye.")
            break

        else:
            print(
                "Unknown command. "
                "Type 'help' to view the available commands."
            )


if __name__ == "__main__":
    main()
