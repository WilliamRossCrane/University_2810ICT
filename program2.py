import math 

# Function to find the word counts 

def count(str): 

        # Create an empty dictionary 

        counts = dict() 

        # Split the line into words 

        words = str.split() 

        # Iterate over each word in line 

        for word in words: 

                # make it uppercase 

                word = word.upper() 

                # Check if the word is already in dictionary 

                if word in counts: 

                        # Increment count of word by 1 

                        counts[word] = counts[word] + 1 

                else: 

      # Add the word to dictionary with count 1 

                        counts[word] = 1 

        # Sorting on the basis of length of words 

        counts = dict(sorted(counts.items(), reverse=True)) 

        # Sorting on the basis of count for words 

        counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True)) 

        # Return the dictionary 

        return counts 

# Function to print the histograms using dictionary 

def printHist(counts): 

        # Get the total number of words 

        # Extract list of counts and then sum it up 

        total = sum(list(counts.values())) 

        # Print the histogram from counts 

        for word in list(counts.keys()): 

                # Find the percentage for the word 

                percent = math.floor(counts[word]*100/total) 

                # Find the number of stars to be printed 

                stars = math.ceil(percent/5) 

                print(f"{word} : [{'*'*stars}] {percent}%") 

if __name__ == "__main__": 

        # Take the input 

        text_file = open("test.txt", "r") 

         #read whole file to a string 

        str = text_file.read() 

        # Get the counts 

        counts = count(str) 

        # Print the histogram 

        print() 

        printHist(counts) 

        print() 