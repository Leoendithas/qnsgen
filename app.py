import streamlit as st
from openai import OpenAI

# Configure page layout (once per page)
st.set_page_config(page_title="Question Generator", layout="wide")

#Font Initialisation
with open( ".streamlit/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

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
        "English": ["-"],
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
    
    "-": [
    "Missing: Adjective",
    "Missing: Adverb",
    "Missing: Conjunction",
    "Missing: Determiner",
    "Missing: Noun",
    "Missing: Particle",
    "Missing: Preposition",
    "Missing: Pronoun",
    "Missing: Punctuation",
    "Missing: Verb",
    "Missing: Contraction",
    "Missing: Word/Phrase",
    "Missing: Possessive",
    "Missing: Verb Form",
    "Missing: Verb Tense",
    "Unnecessary: Adjective",
    "Unnecessary: Adverb",
    "Unnecessary: Conjunction",
    "Unnecessary: Determiner",
    "Unnecessary: Noun",
    "Unnecessary: Particle",
    "Unnecessary: Preposition",
    "Unnecessary: Pronoun",
    "Unnecessary: Punctuation",
    "Unnecessary: Verb",
    "Unnecessary: Contraction",
    "Unnecessary: Space",
    "Unnecessary: Word/Phrase",
    "Unnecessary: Possessive",
    "Unnecessary: Verb Form",
    "Unnecessary: Verb Tense",
    "Unnecessary: Contraction",
    "Replace: Adjective",
    "Replace: Adverb",
    "Replace: Conjunction",
    "Replace: Determiner",
    "Replace: Noun",
    "Replace: Particle",
    "Replace: Preposition",
    "Replace: Pronoun",
    "Replace: Punctuation",
    "Replace: Verb",
    "Replace: Word Form",
    "Replace: Capitalisation",
    "Replace: Word/Phrase",
    "Replace: Spelling",
    "Replace: Word Order",
    "Replace: Noun Number",
    "Replace: Possessive Noun",
    "Replace: Verb Form",
    "Replace: Verb Spelling",
    "Replace: Subject-Verb Agreement",
    "Replace: Verb Tense",
    "Replace: Adjective",
    "Replace: Noun Number",
    "Sentence: Run-On",
    "Sentence: Unnecessary Words",
    "Sentence: Fragment",
    "Collocation: Suggestion"
    ]
}
    return objectives.get(topic)

# Function to generate a prompt based on subject, topic, and learning objective
def create_prompt(subject, topic, learning_objective):
    return f"""You are a seasoned educator who specialises in helping students close their learning gaps.
    Generate five questions along with suggested answers for the skill '{topic}' 
    and skill error that needs to be worked on: '{learning_objective}'
    The subject is '{subject}'.
    Return the questions and suggested answers in bolded headers.
    Do not generate any other text aside from the question and answer.
    """

# Function to call OpenAI API to generate questions and answers
def generate_questions_and_answers(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",  
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

# Function to regenerate selected questions
def regenerate_questions(selected_questions):

    # Get the number of selected questions
    num_questions = len(selected_questions)    

    # Create a new prompt by concatenating selected questions
    prompt = f"""You are a seasoned educator who specialises in helping students close their learning gaps.
    Using the following questions and their answers as reference, 
    generate {num_questions} new question(s) and their suggested answers:
    \n\n""" + "\n\n".join(selected_questions)
    
    
    # Regenerate the questions using OpenAI
    return generate_questions_and_answers(prompt)

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

    # Generate button 123
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
    st.header("Problem Statement")
    st.write("""
        In the current educational landscape, students often receive feedback on their assignments, but this feedback can lack specificity and relevance to their individual mistakes. As a result, many students struggle to consolidate their learning and apply corrections in future assessments. This disconnect not only hinders their academic progress but also leads to increased frustration and disengagement with the learning process. Teachers, too, face challenges; without clear insights into recurring errors, they cannot effectively tailor their interventions or provide targeted support to address individual student needs. The magnitude of this problem is significant, as it affects a large number of students who may repeatedly make the same mistakes without a clear understanding of how to improve. This can result in wasted time and resources, both for the students and for educators who spend hours providing general feedback that does not translate into measurable improvement.    
        """)
    st.image("images/Error Tracking.svg", use_column_width=True)
    st.caption("Teacher's error tracker page which shows what are the most common errors students face.")
    st.header("Proposed Solution")
    st.write("""
To address the challenge of helping students learn from their recurring mistakes, we propose utilizing Large Language Models (LLMs) as a transformative catalyst in the educational process. Much like enzymes that lower activation energy, LLMs can automate the generation of personalized questions based on error tags and past responses, significantly reducing the effort required from educators. By leveraging Retrieval-Augmented Generation (RAG), the model can efficiently pull relevant information and context, allowing it to craft targeted questions that directly address each student's unique challenges. This automation not only streamlines the feedback process but also ensures that students receive immediate, relevant practice opportunities, reinforcing their understanding of key concepts. In addition to lowering the activation energy for learning, the solution promotes the reuse of feedback mechanisms. By establishing a consistent user flow that encourages students to engage with feedback repeatedly, we can foster a habit of reflective learning. Teachers benefit from minimal costs and effort since they are not burdened with the task of creating highly personalized questions. Instead, the LLM can serve as an initial resource, providing a first draft of tailored questions that educators can easily edit.
    """)
    st.header("Impact")
    st.write("""
After implementing the solution, we anticipate noticeable improvements in how students engage with their feedback, leading to a better understanding of key concepts. The system will be used regularly, encouraging students to practice and learn from their mistakes in a manageable way. From an agency or whole-of-government perspective, this approach could save teachers several hours each week on feedback-related tasks, resulting in a meaningful reduction in workload over the year. This streamlined process offers a practical and achievable enhancement to current practices, allowing for more focus on direct student support without making unrealistic promises.    
    """)
    st.header("Project Sponsors & Users")
    st.write("""
This project’s potential impact is significant enough as it aligns with the ongoing efforts to enhance educational outcomes through technology. The integration of the LLM into the existing Student Learning Space (SLS) Feedback Assistant can drive substantial improvements in personalized learning and feedback efficiency, key priorities for educational leadership. The primary users of the LLM applications will be both students and teachers utilizing the SLS platform. Students will benefit directly by receiving targeted questions that help them address their recurring mistakes, while teachers will gain insights into common errors across their classes, enabling them to tailor their interventions effectively. In the long run, the solution has the potential to benefit thousands of users in Singapore, as the SLS is widely adopted among teachers and students, creating a collaborative environment where personalized learning can thrive.    
    """)

# Page: Methodology
def methodology_page():
    st.title("Methodology")
    st.image("images/QnsGen User Flow.jpg", use_column_width=True)

# Page: Home
def home_page():
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>Welcome!</h1>
            <img src="https://r2.flux1.ai/result-YVk9p5WuBq.png" alt="Centered Image" width="400">
            <p>This site is a project for the AI Champions Bootcamp (2024).</p>
        </div>
        """,
        unsafe_allow_html=True
    )
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

import streamlit as st

def display_important_notice():
    # Initialize the session state if 'notice_acknowledged' is not present
    if 'notice_acknowledged' not in st.session_state:
        st.session_state['notice_acknowledged'] = False
    
    # Only display the notice if it hasn't been acknowledged yet
    if not st.session_state['notice_acknowledged']:
        st.info("""
            **IMPORTANT NOTICE**: This web application is developed as a proof-of-concept prototype.
            The information provided here is **NOT** intended for actual usage and should not be relied upon for making any decisions, 
            especially those related to financial, legal, or healthcare matters.

            Furthermore, please be aware that the LLM may generate inaccurate or incorrect information.
            You assume full responsibility for how you use any generated output.

            Always consult with qualified professionals for accurate and personalized advice.
        """)

        # If the button is clicked, set the notice as acknowledged
        if st.button("Acknowledge"):
            st.session_state['notice_acknowledged'] = True

    # No need to rerun manually; Streamlit will automatically handle the rerun

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
