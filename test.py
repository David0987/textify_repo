import streamlit as st


def main():
    st.title("Hello World Streamlit App")
    st.write("Welcome to your first Streamlit app!")

    # Display a simple input box
    user_input = st.text_input("Enter your name:")

    # Display the input value when user submits
    if user_input:
        st.write(f"Hello, {user_input}!")

    # Display a button
    if st.button('Say hello'):
        st.write('Hello, Streamlit user!')

    # Display a slider
    slider_value = st.slider("Choose a number", 0, 100, 50)
    st.write(f"The selected number is: {slider_value}")

    # Display a selectbox
    option = st.selectbox(
        'Choose your favorite programming language',
        ('Python', 'JavaScript', 'C++', 'Java', 'Other')
    )
    st.write(f'Your favorite programming language is: {option}')


if __name__ == "__main__":
    main()



