import streamlit as st
st.title("Calculator")
num1=st.text_input("Enter first number:")
num2=st.text_input("Enter second number:")
add=st.button("Add")
sub=st.button("Subtract")
mul=st.button("Multiply")
div=st.button("Divide")
if add:
    st.success(f"Addition:{int(num1)+int(num2)}")
elif sub:
    st.success(f"Subtraction:{int(num1)-int(num2)}")
elif mul:
    st.success(f"Multiplication:{int(num1)*int(num2)}")
elif div:
    if int(num2)==0:
        st.error("Division not possible.")
    else:
        st.success(f"Division:{int(num1)/int(num2)}")