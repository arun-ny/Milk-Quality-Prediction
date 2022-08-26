
# import base64
from distutils.log import fatal
from pickletools import optimize
# from tkinter import N
import streamlit as st
#from array import array;
import pandas as pd
import numpy as np
import pickle
# import sklearn
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Milk Quality Prediction Home",
    page_icon="🏠",
)

# with st.sidebar:
#    selected = option_menu(
#       menu_title=None,
#       options=["Home","Data","Project Details","Code","Contact"],
#   )

with st.sidebar:
    choose = option_menu("Milk Quality", ["Home", "Data", "Project Details", "Code", "Connect"],
                         icons=['house', 'gem','clipboard-data','text-center', 'link'],
                         menu_icon="app-indicator", default_index=0,
                         styles={"container": {"padding": "5!important", "background-color": "#0E1117"},
                                 "icon": {"color": "orange", "font-size": "25px"},
                                 "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#262730"},
                                 "nav-link-selected": {"background-color": "#FF4B4B"},
                                 }
                         )

if choose == "Home":
    st.markdown(''' 
# Milk Quality Prediction :glass_of_milk:

    ''', True)

    pH = st.slider(label="pH value of Milk", min_value=3.0,
                   max_value=9.5, value=6.8, step=0.1)

    col1, col2 = st.columns(2)

    with col1:
        temp = st.number_input(label="Fill the temperature of Milk",
                               min_value=30, max_value=90, value=42, step=1)
        taste = st.selectbox("Fill the Taste of Milk", ("Good", "Bad"))
        fat = st.selectbox("Fill the Fat content of Milk", ("High", "Low"))

    with col2:
        color = st.number_input("Fill the colour of Milk",
                                min_value=240, max_value=255, value=250, step=1)
        odor = st.selectbox("Fill the Odor of Milk", ("Good", "Bad"))
        turb = st.selectbox("Fill the Turbidity of Milk", ("High", "Low"))

    if taste == "Good":
        _taste = 1
    else:
        _taste = 0

    if fat == "High":
        _fat = 1
    else:
        _fat = 0

    if odor == "Good":
        _odor = 1
    else:
        _odor = 0

    if turb == "High":
        _turb = 1
    else:
        _turb = 0

    inputs = np.array([[pH, temp, _taste, _odor, _fat, _turb, color]])

    file = "model.pkl"
    fileobj = open(file, 'rb')
    model = pickle.load(fileobj)


# with open('model.pkl', 'rb') as f:
#   model = pickle.load(f);

    prediction = model.predict(inputs)

    if prediction == 0:
        _prediction = "High"

    elif prediction == 1:
        _prediction = "Low"

    else:
        _prediction = "Medium"

    Submit = st.button('Predict')

    

    if Submit==True:
        if _prediction == "High":
            st.success(f"The Quality of the given milk is {_prediction}")
        elif _prediction == "Medium":
            st.warning(f"The Quality of the given milk is {_prediction}")
        else:
            st.error(f"The Quality of the given milk is {_prediction}")
        


#st.title("Lets create")

if choose == "Data":
    st.markdown('''
    # Milk Quality Data :glass_of_milk:
    ''')
    data = pd.read_csv("milkdata.csv")
    st.dataframe(data, width=800, height=800)

# if choose == "Code":
    # st.header("The code for the project is below")
    # file = "Milk Quality Prediction pdf.pdf"
    # def displayPDF(file):
    # # Opening file from file path
    #     with open(file, "rb") as f:
    #         base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # # Embedding PDF in HTML
    # pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

    # # Displaying File
    # st.markdown(pdf_display, unsafe_allow_html=True)

if choose == "Code":
    st.header("Jupyter Notebook")
    HtmlFile = open("mqp.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code, height=9500, width=800)

# if choose == "History":
#     st.header("Predicted History")
#     data1 = pd.read_csv("history.csv")
#     st.dataframe(data1, width=800, height=800)

if choose=="Connect":
    st.header("Connect on... :link:")
    st.subheader("Heroku Link")
    st.success("https://milkqualityprediction-arun.herokuapp.com")
    st.subheader("GitHub Link")
    st.success("https://github.com/arun-ny/Milk-Quality-Prediction")

if choose == "Project Details":
    st.header("Details about project")
    st.subheader("About Data")
    st.write("This dataset consists of 7 independent variables ie pH, Temperature, Taste, Odor, Fat, Turbidity, and Color. Generally, the Grade or Quality of the milk depends on these parameters. These parameters play a vital role in the predictive analysis of the milk.")
    st.markdown(
        '''
        ### pH
        ###### The pH value for fresh raw milk is normally in the range of 6.4 to 6.8 and depends on the source of the milk. The pH of milk accounts for the amount of lactic acid produced by microbial activity. The more lactic acid present, the higher the acidity. This would result in a change in taste and smell, making it unsuitable for human consumption. pH is an important quality parameter in the dairy industry. The quality of raw milk, as well as essentially the finished product, must be monitored and maintained in any dairy industry, whether during packaging for human consumption or subsequent processing of other dairy products.
        '''
    )
    st.markdown(
        '''
        ### Temperature
        ###### Here is some information and tips for storing and serving milk at home to keep it fresh as long as possible:
        ###### 1. While at the grocery store, pick up milk last so it stays as cool as possible. Refrigerate promptly after you get home.
        ###### 2. Ideally, milk should be stored in the refrigerator at 40 degrees F or below. Storing and serving milk at this temperature extends overall shelf-life and maximizes flavor.
        ###### 3. Store your milk in the coldest part of the refrigerator, not in the door where it will be exposed to outside air every time someone opens it.

        '''
    )

    st.markdown(
        '''
        ### Taste
        ###### The taste of milk, as this word is commonly used, is the sensation perceived when milk is taken into the mouth. The term “flavor,” as used in this paper, is a combination of the sensations of taste, perceived in the mouth, with those of smell, produced through the medium of the inner nasal passages. It has aided in precision to confine the term “taste” to those sensations which are perceived only in the mouth.

        ###### In our dataset 
        ###### 0 -> Bad Taste
        ###### 1-> Good Taste
        '''
    )

    st.markdown(
        '''
        ### Odor
        ###### Good quality milk should have a pleasantly sweet and clean flavor with no distinct aftertaste. Because of the perishability of milk and the nature of milk production and handling procedures, the development of off- flavors/odors is not uncommon. To prevent flavor/odor defects in milk, proper milk handling procedures from the farm to the consumer are essential. 
        ###### In our dataset 
        ###### 0 -> Bad Odor
        ###### 1-> Good Odor
        
        
        '''
    )

    st.markdown(
        '''
        ### Fat Content
        ###### When you shop in the dairy case, the primary types of milk available are whole milk (3.25% milk fat), reduced-fat milk (2%), low-fat milk (1%) and fat-free milk, also known as skim milk. Each one packs 13 essential nutrients, including 8 grams of high-quality protein. Types of milk vary by percentage of milkfat, or the amount of fat that is in the milk by weight. These percentages are noted on the package and by the different cap colors to show the milkfat at a glance.
        ###### In our dataset 
        ###### 0 -> Low Fat Content
        ###### 1-> High Fat Content
        '''
    )

    st.markdown(
        '''
        ### Turbidity
        ###### The turbidity per unit concentration of total solids varies with the fat content of the milk and also with the efficiency of homogenization since about three- fourths of the total turbidity can be attributed to the fat phase. When the turbidity due to the non-fat portion of the milk has been reduced to a negligible quantity by the addition of ammonia, the turbidity of the fat globules per unit concentration of fat is shown to be closely related to the particle size distribution.
        ###### In our dataset 
        ###### 0 -> Low Turbidity
        ###### 1-> High Turbidity
        
        
        '''
    )

    st.markdown(
        '''
        ### Color
        ###### Milk is a natural, whole food made up of water, protein, fat, carbohydrates in the form of lactose, vitamins including calcium, minerals including phosphorous and a range of other bioactive compounds.
        ###### Color code ranges from 240 to 255.
        
        '''
    )






