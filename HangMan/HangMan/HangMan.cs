using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;


namespace HangMan
{
    public delegate void MyEventHandler(int x);
    class HangMan
    {
        private HangManBoard currentBoard = new HangManBoard();

        private string secretWord;

        private List<string> lettersGuessed = new List<string> { };

        private int wrongGuessed = 0;

        private List<string> guessWordLines = new List<string> { };

        public HangMan(string myWord)
        {
            secretWord = myWord.ToLower();

            for (int i = 0; i < secretWord.Length; i++)
            {
                guessWordLines.Add("-");
            }

        }

        private bool HasWon()
        {
            if (ShowWordSoFar() == secretWord)
            {
                return true;
            }
            return false;
        }

        public void DisplayIntro()
        {
            StringBuilder sb = new StringBuilder();
            sb.AppendLine("Welcome to HangMan (in this case draw dog).");
            sb.AppendLine("To play, guess a letter to try to guess the word.");
            sb.AppendLine("Every time you choose an incorrect letter another dog body part appears.");
            sb.AppendLine("If you guess the  word before you get a barking dog, you win :-)");
            sb.AppendLine("If you lose you get a dog barking at you :-( ");
            sb.AppendLine();
            sb.AppendLine(@"NOTE: The board is intially 'EMPTY' and will start to fill in as the game continues.");
            sb.AppendLine();
            Console.WriteLine(sb);
        }

        public void DisplayPlayerStats()
        {
            currentBoard.ShowBoard();
            //show current word so far and number of wrong guesses
            Console.WriteLine("Letters guessed already => {0}", ShowLettersGuessed());
            Console.WriteLine("Number of wrong guesses => {0}", wrongGuessed);
            Console.WriteLine("Word so far => {0}", ShowWordSoFar());
        }

        private string ShowWordSoFar()
        {
            string myWordSoFar = string.Join("", guessWordLines);
            return myWordSoFar;
        }

        private string ShowLettersGuessed()
        {
            string myLettersGuessed = string.Join(" ", lettersGuessed);
            return myLettersGuessed;
        }

        private void GuessLetter(string letter)
        {
            if (lettersGuessed.Contains(letter))
            {
                Console.WriteLine("Enter a letter you haven't already guessed.");
                return;
            }
            if (secretWord.Contains(letter))
            {
                //If word contains letter, update my word so far and letters guessed
                lettersGuessed.Add(letter);

                for (int i = secretWord.IndexOf(letter); i > -1; i = secretWord.IndexOf(letter, i + 1))
                {
                    guessWordLines[i] = letter;
                }
                return;
            }
            else
            {
                //if a wrong guess, update number of wrong guesses and letters guessed
                //and update board
                wrongGuessed += 1;
                lettersGuessed.Add(letter);
                currentBoard.Update(wrongGuessed);
                return;
            }
        }

        public string GetLetter()
        {
            string userInput;
            //get user input
            userInput = Console.ReadLine().Trim().ToLower();
            //check input
            while (!Regex.IsMatch(userInput, @"^[a-zA-Z]+$") || userInput.Length != 1)
            {
                Console.WriteLine("Please enter a single letter from the English alphabet (A-Z).");
                userInput = Console.ReadLine().Trim().ToLower();
            }
            return userInput;
        }

        public void Play()
        {
            Console.WriteLine("Time to Guess!");
            Console.WriteLine();

            do
            {
                //display stats each round
                DisplayPlayerStats();
                Console.WriteLine();

                //user input
                Console.Write("Choose a letter => ");
                var userLetter = GetLetter();

                GuessLetter(userLetter);

                if (HasWon() == true)
                {
                    Console.WriteLine("You Win!");
                    return;
                }
            } while (wrongGuessed != 6);

            currentBoard.ShowBoard();
            Console.WriteLine("You Loose.");
        }

    }
}
