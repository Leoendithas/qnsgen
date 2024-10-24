import streamlit as st
from openai import OpenAI

# Initialize the OpenAI API key
client = OpenAI(api_key=st.secrets["api_keys"]["openai"])

# Function to dynamically fetch topics based on the selected subject
def get_topics(subject):
    topics = {
        "Mathematics": [
 'ExpandDoubleDifferenceSquares',
 'ExpandDoubleBracketsMultiplication',
 'ExpandDoubleBracketsSquare',
 'ExpandSingleBrackets',
 'FactorDoubleDifferenceSquares',
 'FactorIdentitySquare',
 'FactorDoubleSumProduct',
 'FactorSingleBrackets',
 'AlgebraAddingLikeTerms',
 'AlgebraPowerNegativeExponent',
 'AlgebraDivisionOfPowerFunctions',
 'AlgebraPowerOfProduct',
 'AlgebraProductOfPowerFunctions',
 'AlgebraProductOfRoots',
 'FractionArithmeticAddMixed',
 'FractionArithmeticAddProperCommonDenominator',
 'FractionArithmeticAddProperUnlikeDenominator',
 'FractionArithmeticSubtractMixed',
 'FractionArithmeticDivisionProper',
 'FractionArithmeticEquivalentConcept',
 'FractionArithmeticSimilarMixed',
 'FractionArithmeticMultiplicationMixed',
 'FractionArithmeticMultiplicationProper',
 'EquationsBalanceMethodArrangeTerms',
 'EquationsSplitFactors',
 'EquationsFactorLHS',
 'EquationsInvertingPower',
 'EquationsOperationsAdd',
 'EquationsOperationsMultiply',
 'EquationsOperationsPower',
 'EquationsQuadraticFormulaDiscriminant',
 'RoundingDecimals'
],
        "English": ["Add", "Remove", "Replace", "Sentence", "Collocation"],
    }
    return topics.get(subject, ["General Topic"])

# Function to dynamically fetch learning objectives based on the selected topic
def get_learning_objectives(topic):
    objectives = {
    "ExpandDoubleDifferenceSquares": ["SignError"],
    "ExpandDoubleBracketsMultiplication": ["NoCrossTerms", "MissingTerms"],
    "ExpandDoubleBracketsSquare": ["NoCrossTerms"],
    "ExpandSingleBrackets": ["DoubleMultiplication", "SkippingTerms", "SignError", "MissingBrackets"],
    "FactorDoubleDifferenceSquares": ["SignError"],
    "FactorIdentitySquare": ["SignError"],
    "FactorDoubleSumProduct": ["SwitchedSumProduct"],
    "FactorSingleBrackets": ["SignError", "SkippingTerms"],
    "AlgebraAddingLikeTerms": ["UnlikeTerms"],
    "AlgebraPowerNegativeExponent": ["ChangingTermType"],
    "AlgebraDivisionOfPowerFunctions": ["DividingExponents", "DifferentBase"],
    "AlgebraPowerOfProduct": ["SignError", "NotAllFactors"],
    "AlgebraProductOfPowerFunctions": ["MultiplyingExponents", "DifferentBase"],
    "AlgebraProductOfRoots": ["MultiplyingFactor"],
    "FractionArithmeticAddMixed": ["AddedDenominator", "IncorrectFractionalPart", "IncorrectIntegerPart"],
    "FractionArithmeticAddProperCommonDenominator": ["AddedDenominator"],
    "FractionArithmeticAddProperUnlikeDenominator": ["AddedDenominator", "SubtractedDenominator"],
    "FractionArithmeticSubtractMixed": ["AddedDenominator", "AddedFractionalPart"],
    "FractionArithmeticDivisionProper": ["NotFlippingFraction", "FlippingWrongFraction", "FlippingBothFractions", "SubtractionInsteadOfDivision"],
    "FractionArithmeticEquivalentConcept": ["EquivalentEqual", "EquivalentNumerator", "EquivalentNumeratorDenominator"],
    "FractionArithmeticSimilarMixed": ["MixedFractionConcept"],
    "FractionArithmeticMultiplicationMixed": ["MultiplyingFractionalPartOnly"],
    "FractionArithmeticMultiplicationProper": ["CreatingSimilarFractionsToMultiply"],
    "EquationsBalanceMethodArrangeTerms": ["CrossMultiplicationDone", "ArrangeToZero"],
    "EquationsSplitFactors": ["SplitFactorOnNonzeroRHS"],
    "EquationsFactorLHS": ["FactorDivide"],
    "EquationsInvertingPower": ["IncorrectOrder", "MissingSecondSolution", "ExtraSecondSolution", "InvalidSecondSolution"],
    "EquationsOperationsAdd": ["AddSubtract"],
    "EquationsOperationsMultiply": ["MultiplyOneSide", "MultiplyAllTerms"],
    "EquationsOperationsPower": ["SignError", "FlipSign", "MissingBrackets"],
    "EquationsQuadraticFormulaDiscriminant": ["MixedCoefficients"],
    "RoundingDecimals": ["RoundErrorUpDown"],
    "Add": [
        "Adjective",
        "Adverb",
        "Conjunction",
        "Determiner",
        "Noun",
        "Particle",
        "Preposition",
        "Pronoun",
        "Punctuation",
        "Verb",
        "Contraction",
        "Word/Phrase",
        "Possessive",
        "Verb Form",
        "Verb Tense"
    ],
    "Remove": [
        "Adjective",
        "Adverb",
        "Conjunction",
        "Determiner",
        "Noun",
        "Particle",
        "Preposition",
        "Pronoun",
        "Punctuation",
        "Verb",
        "Contraction",
        "Space",
        "Word/Phrase",
        "Possessive",
        "Verb Form",
        "Verb Tense"
    ],
    "Replace": [
        "Adjective",
        "Adverb",
        "Conjunction",
        "Determiner",
        "Noun",
        "Particle",
        "Preposition",
        "Pronoun",
        "Punctuation",
        "Verb",
        "Contraction",
        "Word Form",
        "Capitalisation",
        "Word/Phrase",
        "Spelling",
        "Word Order",
        "Noun Number",
        "Possessive Noun",
        "Verb Form",
        "Verb Spelling",
        "Subject-Verb Agreement",
        "Verb Tense"
    ],
    "Sentence": [
        "Long",
        "Unnecessary Words",
        "Fragment"
    ],
    "Collocation": [
        "Suggestion"
    ]
}
    return objectives.get(topic)

# Function to generate a prompt based on subject, topic, and learning objective
def create_prompt(subject, topic, learning_objective):
    return f"""Generate five questions along with suggested answers for the subject '{subject}', 
    skill '{topic}', and skill error that needs to be worked on: {learning_objective}.
    Return the questions and suggested answers in bolded headers.
    """

# Function to call OpenAI API to generate questions and answers
def generate_questions_and_answers(prompt):
    response = client.chat.completions.create(
        model="gpt-4",  # Use GPT-4 if available
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=400,
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

# Function to regenerate selected questions
def regenerate_questions(selected_questions):
    # Create a new prompt by concatenating selected questions
    prompt = "Using the following questions and their answers as reference, generate new question and their suggested answers based on the number of questions indicated:\n\n" + "\n\n".join(selected_questions)
    
    # Regenerate the questions using OpenAI
    return generate_questions_and_answers(prompt)

# Configure page layout
st.set_page_config(page_title="Question Generator", layout="wide")

# Define pages
def generate_questions_page():
    st.title("Generate Questions")

    # Subject dropdown 
    subjects = [
        "Mathematics", "English"
    ]
    
    # Subject selection
    selected_subject = st.selectbox("Choose a subject:", subjects)

    # Fetch the relevant topics based on selected subject
    topics = get_topics(selected_subject)

    # Topic selection dropdown (renamed from Learning Objective)
    selected_topic = st.selectbox("Choose a skill:", topics)

    # Fetch the relevant learning objectives based on selected topic
    learning_objectives = get_learning_objectives(selected_topic)

    # Learning Objective selection dropdown (new dropdown)
    selected_learning_objective = st.selectbox("Choose a skill error:", learning_objectives)

    # Store generated and regenerated questions in session state to persist them across interactions
    if 'questions_and_answers' not in st.session_state:
        st.session_state['questions_and_answers'] = []

    if 'regenerated_questions' not in st.session_state:
        st.session_state['regenerated_questions'] = []

    # Generate button
    if st.button("Generate Questions"):
        if selected_subject and selected_topic and selected_learning_objective:
            # Create the prompt
            prompt = create_prompt(selected_subject, selected_topic, selected_learning_objective)

            # Generate questions and answers
            with st.spinner("Generating questions and answers..."):
                questions_and_answers = generate_questions_and_answers(prompt)

            # Format the response for better readability (New lines for question vs answer and bold headers)
            formatted_qas = []
            qas_list = questions_and_answers.split("\n\n")
            for i, qa in enumerate(qas_list):
                # Insert new lines between question and answer and bold the headers
                formatted_qa = qa.replace('Q:', '**Question:**\n').replace('A:', '\n**Suggested Answer:**\n')
                formatted_qas.append(formatted_qa)

            # Store the formatted questions and answers in session state
            st.session_state['questions_and_answers'] = formatted_qas

    # Only display the questions and answers after they are generated
    if st.session_state['questions_and_answers']:
        st.subheader("Generated Questions and Suggested Answers")

        # "Select All" checkbox for generated questions
        select_all = st.toggle("Select All Generated Questions")

        # Display generated questions with individual checkboxes
        selected_for_saving = []
        for i, qa in enumerate(st.session_state['questions_and_answers']):
            if select_all:
                selected_for_saving.append(qa)
                st.checkbox(qa, value=True, key=f"qa_{i}", disabled=True)  # Keep the actual generated QA text
            else:
                if st.checkbox(qa, key=f"qa_{i}"):
                    selected_for_saving.append(qa)
        
        # Show Save and Regenerate buttons even if no checkboxes are selected
        col1, col2 = st.columns(2)

        with col1:
            # Save button
            if st.button("Save Selected Questions"):
                if 'saved_questions' not in st.session_state:
                    st.session_state['saved_questions'] = []
                st.session_state['saved_questions'].extend(selected_for_saving)
                st.success(f"Saved {len(selected_for_saving)} question(s) and answer(s)!")

        with col2:
            # Regenerate button
            if st.button("Regenerate Selected Questions"):
                if selected_for_saving:
                    with st.spinner("Regenerating selected questions..."):
                        regenerated_questions = regenerate_questions(selected_for_saving)
                    
                    # Format the regenerated questions and store them in session state
                    formatted_regenerated_qas = []
                    qas_list = regenerated_questions.split("\n\n")
                    for i, qa in enumerate(qas_list):
                        formatted_qa = qa.replace('Q:', '**Question:**\n').replace('A:', '\n**Suggested Answer:**\n')
                        formatted_regenerated_qas.append(formatted_qa)

                    # Store regenerated questions in session state
                    st.session_state['regenerated_questions'] = formatted_regenerated_qas

    # Display regenerated questions if available
    if st.session_state['regenerated_questions']:
        st.subheader("Regenerated Questions and Suggested Answers")
        
        # Use checkboxes for regenerated questions
        selected_for_saving_regenerated = []
        for i, qa in enumerate(st.session_state['regenerated_questions']):
            if st.checkbox(qa, key=f"regenerated_qa_{i}"):
                selected_for_saving_regenerated.append(qa)

        # Save regenerated questions
        if st.button("Save Regenerated Questions"):
            if 'saved_questions' not in st.session_state:
                st.session_state['saved_questions'] = []
            st.session_state['saved_questions'].extend(selected_for_saving_regenerated)
            st.success(f"Saved {len(selected_for_saving_regenerated)} regenerated question(s) and answer(s)!")

def view_saved_questions_page():
    st.title("View Saved Questions")
    if 'saved_questions' in st.session_state and st.session_state['saved_questions']:
        for saved_qa in st.session_state['saved_questions']:
            st.write(saved_qa)
    else:
        st.info("No questions have been saved yet.")

# Page: About Us
def about_us_page():
    st.title("About Us")
    st.write("""
        Welcome to the Question Generator! This page is designed to generate questions
        based on error tags selected by teachers. This will allow teachers to follow up on student's mistakes and
        improve student learning outcomes.
    """)

# Page: Methodology
def methodology_page():
    st.title("Methodology")
    st.header("Problem Statement")
    st.write("""
        Teachers can track student's errors using the new error tag features, 
        but might not have the resources to follow up on student's errors.
    """)
    st.header("Proposed Solution")
    st.write("""
        Teachers can use the Question Generator to follow up on student's errors through generating
        questions that specifically target the student's learning gaps. Teachers can save the questions generated, or
        regenerate should they find the questions not suitable.

        Thereafter, they can deploy the questions to students for practice and further assessment for learning.
    """)

# Page: Home
def home_page():
    st.title("Welcome!")
    st.image("https://r2.flux1.ai/result-YVk9p5WuBq.png", width=400)
    st.write("""
        This site is a project for the AI Champions Bootcamp (2024).
    """)
    st.subheader("Context")
    st.write("""
        Assessment for learning is part and parcel of a teacher's life. After marking their students' work, teachers spend time analysing student's mistakes and identifying learning gaps to follow up on.
        Thereafter, they have to look for resources to cover these learning gaps.
        However, resources may be scarce or may not be well classified.
        """)
    st.subheader("Proposed Solution")
    st.write("""
        The Question Generator seeks to smoothen this process by having an LLM generate follow-up questions based on the 'Error Tags' indicated on SLS.
        These error tags are represented by the 'Skills' that need to be learnt, as well as the 'Skill Error' commonly committed by students for that concept.
        
        Teachers can save the questions generated, or regenerate new ones should they find the questions not suitable.    
        Thereafter, they can deploy the questions to students for practice and further assessment for learning.
            
        **We hope this will help teachers to better close learning gaps for their students.**

        Best, 
        Lance & Addie
        """)
# Function to display the important notice
def display_important_notice():
    # Display the notice only if the user hasn't acknowledged it
    if 'notice_acknowledged' not in st.session_state:
        st.session_state['notice_acknowledged'] = False
    
    # If notice is not acknowledged, show the popup
    if not st.session_state['notice_acknowledged']:
            st.info("""
                **IMPORTANT NOTICE**: This web application is developed as a proof-of-concept prototype.
                The information provided here is **NOT** intended for actual usage and should not be relied upon for making any decisions, 
                especially those related to financial, legal, or healthcare matters.

                Furthermore, please be aware that the LLM may generate inaccurate or incorrect information.
                You assume full responsibility for how you use any generated output.

                Always consult with qualified professionals for accurate and personalized advice.
            """)

            # Acknowledge button
            if st.button("Acknowledge"):
                st.session_state['notice_acknowledged'] = True  # Set the session state to True to not show the message again

# Main function where the notice is displayed and other page logic is handled
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a page:", ["Home", "Generate Questions", "View Saved Questions", "Methodology", "About Us"])

    # Display the important notice only on the first visit (or until acknowledged)
    display_important_notice()

    # Page routing
    if page == "Home":
        home_page()
    elif page == "Generate Questions":
        generate_questions_page()
    elif page == "View Saved Questions":
        view_saved_questions_page()
    elif page == "About Us":
        about_us_page()
    elif page == "Methodology":
        methodology_page()

if __name__ == "__main__":
    main()
