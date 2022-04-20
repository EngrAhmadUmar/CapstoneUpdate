import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Home")

    st.markdown(
        """
   Cardiovascular disease is a broad term that refers to various conditions that can affect your heart. According to the World Health Organization, 17.9 million people die each year from CVDs (cardiovascular diseases). It is the leading cause of death among adults. With their medical history, this project can help forecast who is likely to be diagnosed with heart disease. It recognizes who has any heart disease symptoms, such as chest pain or high blood pressure, and can assist in detecting the disease with fewer medical tests and more effective therapies, allowing them to be treated appropriately. The development of a system based on logistic regression is a superior solution to the current challenges that medical specialists and patients confront while detecting heart disease. As a result, the system would be built to minimize the death rate from cardiac problems while also boosting the rate of successful detection. Due to the neural network system, medical experts' errors, such as misdiagnoses, would be removed, and a prompt prevention strategy may destroy the disease at its core. However, to construct such a model, this research would be structured around a specific dataset that would essentially contain the diagnosis data of numerous people who had previously been diagnosed with heart disease. 
The development of a model for reliably and effectively identifying heart illness has become crucial in light of the rising number of deaths due to heart failure. Providing reliable facilities at reasonable pricing is a significant issue for healthcare institutions (healthcare centers, hospital clinics). The present models' major issues are accuracy, usefulness, and reliability. This study aims to create a system based on logistic regression that will address the present obstacles that medical specialists and people have when it comes to diagnosing heart disease. Consequently, the system would be built to minimize the death rate from cardiac problems while also boosting the rate of successful detection.


    """
    )
