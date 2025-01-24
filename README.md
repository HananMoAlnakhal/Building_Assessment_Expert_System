# **Building Assessment Expert System**  
### A Rule-Based Expert System Using Fuzzy Logic for Building Damage Assessment  

[Visit the Application Here](https://building-assessment-expert-system.onrender.com/)

---

## **About the Project**  
- this system has 2 subsystems :
  - one for getting the damage percentage
  - the other is for getting the habitability and repairability from the damage percentage and the age
  
This is a **rule-based expert system** that uses more than 44+ Rules designed for **building damage assessment**. It uses **fuzzy logic** to handle uncertainty and imprecision in the assessment process. Using Python's `skfuzzy` library for fuzzy logic and Flask for the user interface, this system offers a streamlined way to evaluate building conditions based on key input factors.
The system provides damage severity, habitability, and repair recommendations.  

---

## **Features**  
- **Fuzzy Logic Implementation**: Utilize Python's `scikit-fuzzy` for flexible and robust fuzzy logic inference.  
- **Rule-Based Reasoning**: Assess building damage based on predefined expert rules and decision matrices.  
- **Uncertainty Management**: Handle ambiguous data effectively.  
- **Interactive User Interface**: Developed using Flask for a seamless user experience.  
- **Real-Time Output Visualization**: Results include severity percentages, habitability evaluations, and repair recommendations.

---

## **Live Application**  
You can try the live application here:  
[**Building Assessment Expert System**](https://building-assessment-expert-system.onrender.com/)  

---

## **Project Structure**  
```
BUILDING_ASSESSMENT_EXPERT_SYSTEM/
│
├── flask_app/                    # Main Flask application
│   ├── templates/                # HTML templates for the Flask UI        
│   │   └── index.html            # Main HTML file
│   ├── damage_assessment_api.py  # Flask API for assessments
│   ├── ES.py                     # Expert system core logic
│   └── requirements.txt          # List of Python dependencies
│
├── plots/                        # Visualizations and analysis plots
│   ├── areaVScol.png
│   ├── areaVSrubble_percentage.png
│   ├── Habitability.png
│   ├── hightVSrubble_percentage.png
│   └── Repairability.png
│
├── .gitattributes                # Git attributes for repository
└── fuzzy_expert_system.ipynb     # Jupyter Notebook for development and testing
```
> You can explore the provided notebook for fuzzy ES. code explaination
---
## **Test Cases from the *Notebook***:
**Case 1**
| Input for the first ES  |value|
|--------------------------|------|
|building_hight            | 3 floors    |
|ruble_percentage          |  0.20      |
|building_area         |  250      |
|intact_col         |  2      |
|tilt         |  0      |

|Damage|val|
|-------|----|
|0.38|Moderate|

after getting the damage we use it in the other sys as following:
| Input for the first ES  |value|
|--------------------------|------|
|building damage            | 0.23    |
|building_age          |  60 years      |

|Output|val|
|-------|----|
|habitability|prohibited|
|reparability| Strengthening|

the damage output:
![image](https://github.com/user-attachments/assets/4a6851e9-e362-48a2-8ae0-725b7e24025c)


## **Technologies Used**  
- **Python 3.8+**  
- **Flask**: Web framework for creating the UI and API.  
- **scikit-fuzzy**: Python library for fuzzy logic and uncertainty modeling.  
- **Matplotlib**: For data visualization and graphing results.  

---

## **Contributing**  
Contributions are welcome! If you’d like to improve this project, feel free to:  
1. Fork the repository.  
2. Create a new branch 
3. Commit your changes 
4. Push to your branch 
5. Open a Pull Request.

---
## **Contact**  
For questions, feedback, or suggestions, feel free to contact me:  
- **Email**: halnakhal1@smail.ucas.edu.ps 
- **GitHub**: [HananMoAlnakhal Profile](https://github.com/HananMoAlnakhal)  
