using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HangMan
{
    public class HangPersonGames
    {
        /// <summary>
        /// Takes in a text file containing a signle word
        /// to be played in classic Hang Man game.
        /// </summary>
        /// <param name="args"> Must have file path</param>
        static void Main(string[] args)
        {
            string filePath = (@args[0]);
            string mySecretWord;
            try
            {
                using (var reader = new StreamReader(filePath))
                {

                    mySecretWord = reader.ReadLine().Trim();
                }
            }
            catch(Exception e)
            {
                Console.WriteLine("System could not find file. Please try again, typing in a correct file location.", e.Message);
                Console.ReadKey();
                return;
            }
            string answer;
            do
            {
                HangMan game = new HangMan(mySecretWord);
                game.DisplayIntro();
                game.Play();
                Console.Write(@"Do you want to play again? (y/n) ");
                answer = (Console.ReadLine().ToLower());
            } while (answer.StartsWith("y"));

            Console.WriteLine();
            Console.WriteLine("Thanks For Playing!");
            Console.WriteLine();
        }
    }
}
