import pandas as pd
import API_Functions

def main_func():
    # Category Display
    category_Dict = {
        1: "Spells",
        2: "Monsters",
        3: "Magic Items"
        # 4: "Feats",
        # 5: "Races",
        # 6: "Classes",
        # 7: "Weapons"
    }
    categories_df = pd.DataFrame.from_dict(category_Dict, orient='index')
    categories_df = categories_df.rename(columns={0: "Section"})
    print(categories_df)

    # Section selection
    print("\nInput number for corresponding section:")

    def section_input():
        try:
            section = int(input())
            if 0 < section < (len(category_Dict) + 1):
                section = int(section) - 1
                return int(section)
            else:
                print("Please enter a value from 1 to " + str(len(category_Dict)))
                return section_input()
        except:
            print("Please input an integer:")
            return section_input()

    section = section_input()

    API_Functions.nested_func(idx=section)

    def run_again(question):
        reply = str(input(question + '(y/n): ')).lower().strip()
        if reply == 'y':
            rerun = True
            return main_func()
        if reply == 'n':
            return
        else:
            print("Please just use lowercase y/n")
            return run_again(question)

    run_again("\nWould you like to search for another topic?\n")


if __name__ == "__main__":
    main_func()
