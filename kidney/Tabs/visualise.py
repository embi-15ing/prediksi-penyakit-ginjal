import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn import tree
import streamlit as st

from web_functions import train_model

def app(df,x,y):

	warnings.filterwarnings('ignore')
	st.set_option('deprecation.showPyplotGlobalUse', False)

	st.title("Visualisasi Prediksi Batu Ginjal")

	if st.checkbox("Plot Confusion Matrix"):
	    model, score = train_model(x, y)
	    y_pred = model.predict(x)  # Assuming x is your input data
	    cm = confusion_matrix(y, y_pred)
	    plt.figure(figsize=(10, 6))
	    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
	    plt.xlabel("Predicted")
	    plt.ylabel("True Label")
	    st.pyplot()


	if st.checkbox("Plot Decision Tree"):
	    model, score = train_model(x, y)
	    dot_data = tree.export_graphviz(
	        decision_tree=model, max_depth=4, out_file=None, filled=True, rounded=True,
	        feature_names=x.columns, class_names=['nockd', 'ckd']
	    )

	    st.graphviz_chart(dot_data)

