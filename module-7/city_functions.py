#Format below adapted from:
#Python Crash Course: A Hands-On, Project-Based Introduction to Programming, 2nd Edition
#by Eric Matthes
#Chapter 11 name_function.py

def get_formatted_name(city, country, language='', population='' ):
    if population and language:
        full_name = f"{city}, {country}, population: {population}, {language}"
    elif population:
        full_name = f"{city}, {country}, population: {population}"
    elif language:
        full_name = f"{city}, {country}, {language}"
    else:
        full_name = f"{city}, {country}"
    return full_name.title()

#Format below adapted from:
#Python Crash Course: A Hands-On, Project-Based Introduction to Programming, 2nd Edition
#by Eric Matthes
#Chapter 11 names.py

def output_to_user():
    print("Enter 'q' at any time to quit.")
    while True:
        city = input("\nPlease enter a city: ")
        if city == 'q':
            break
        country = input("Please enter a country: ")
        if country == 'q':
            break
        population = input("Please enter the population (hit enter to skip): ")
        if population == 'q':
            break
        language = input("Please enter the language (hit enter to skip): ")
        if language == 'q':
            break

        formatted_name = get_formatted_name(city, country, language, population)
        print(f"\tNeatly formatted name: {formatted_name}.")

if __name__ == '__main__':
       output_to_user()