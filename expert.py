def diagnose(symptoms):
    if "fever" in symptoms and "cough" in symptoms and "breath" in symptoms:
        return "You might have symptoms of COVID-19. Please get tested immediately."
    elif "fever" in symptoms and "headache" in symptoms and "vomit" in symptoms:
        return "You may have dengue or malaria. Please consult a physician."
    elif "chest pain" in symptoms and "breath" in symptoms:
        return "You may have a heart-related issue. Please visit a cardiologist."
    elif "stomach pain" in symptoms and "vomit" in symptoms:
        return "You might have a stomach infection or food poisoning."
    elif "rash" in symptoms and "itching" in symptoms:
        return "You might have a skin allergy or infection. Consider seeing a dermatologist."
    elif "sore throat" in symptoms and "cough" in symptoms:
        return "You may have a common cold or flu."
    else:
        return "Symptoms not recognized. Please consult a general physician for further diagnosis."

def expert_system():
    print("Welcome to MedBot - Expert Medical Diagnosis Assistant")
    print("Please describe your symptoms separated by commas (e.g., fever, cough, headache):")
    
    input_symptoms = input("Your Symptoms: ").lower().split(',')
    symptoms = [s.strip() for s in input_symptoms]

    result = diagnose(symptoms)
    print("\nDiagnosis Result:")
    print(result)

# Run the Expert System
expert_system()
