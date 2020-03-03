using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HangMan
{
    public class HangManBoard
    {
        private StringBuilder board = new StringBuilder();

        public HangManBoard()
        {
            board.AppendLine(" ____________________________");
            board.AppendLine("|                            |");
            board.AppendLine("|                            |");
            board.AppendLine("|                            |");
            board.AppendLine("|                            |");
            board.AppendLine("|-----------EMPTY------------|");
            board.AppendLine("|                            |");
            board.AppendLine("|                            |");
            board.AppendLine("|                            |");
            board.AppendLine("|____________________________|");
        }

        public void Update(int x)
        {
            //update to dictionary and event 
            if (x == 1)
            {
                Tail();
            }
            else if (x == 2)
            {
                TailAndHead();
            }
            else if (x == 3)
            {
                Body();
            }
            else if (x == 4)
            {
                LegLeft();
            }
            else if (x == 5)
            {
                LegRight();
            }
            else if (x == 6)
            {
                Bark();
            }
        }
        public void ShowBoard()
        {
            Console.WriteLine(board);
        }

        private void Tail()
        {
            StringBuilder tail = new StringBuilder();
            tail.AppendLine(" / __ \\   "); //use of escape keys
            tail.AppendLine(" ||  |/    ");
            tail.AppendLine(" ||        ");//use of literal
            tail.AppendLine(" ||        ");
            board = tail;
        }

        private void TailAndHead()
        {
            StringBuilder tailAndHead = new StringBuilder();
            tailAndHead.AppendLine(" / __ \\             |\\___"); //use of escape keys
            tailAndHead.AppendLine(" ||  |/             /    \\___");
            tailAndHead.AppendLine(" ||                |       __|");//use of literal
            tailAndHead.AppendLine(" ||                |      /   ");
            board = tailAndHead;
        }

        private void Body()
        {
            StringBuilder body = new StringBuilder();
            body.AppendLine(" / __ \\             |\\___"); //use of escape keys
            body.AppendLine(" ||  |/             /    \\___");
            body.AppendLine(" ||                |       __|");//use of literal
            body.AppendLine(" ||                |      /     ");
            body.AppendLine(@" \ \______________/      |  ");
            body.AppendLine("  |                      |   ");
            body.AppendLine("  | __________________  /   ");

            board = body;
        }

        private void LegLeft()
        {
            StringBuilder legLeft = new StringBuilder();
            legLeft.AppendLine(" / __ \\             |\\___"); //use of escape keys
            legLeft.AppendLine(" ||  |/             /    \\___");
            legLeft.AppendLine(" ||                |       __|");//use of literal
            legLeft.AppendLine(" ||                |      /     ");
            legLeft.AppendLine(@" \ \______________/      |  ");
            legLeft.AppendLine("  |                      |   ");
            legLeft.AppendLine("  | __________________  /   ");
            legLeft.AppendLine("  ||                    ");
            legLeft.AppendLine("  ||                    ");
            legLeft.AppendLine(@"  \\                   ");

            board = legLeft;
        }

        private void LegRight()
        {
            StringBuilder legRight = new StringBuilder();
            legRight.AppendLine(" / __ \\             |\\___"); //use of escape keys
            legRight.AppendLine(" ||  |/             /    \\___");
            legRight.AppendLine(" ||                |       __|");//use of literal
            legRight.AppendLine(" ||                |      /     ");
            legRight.AppendLine(@" \ \______________/      |  ");
            legRight.AppendLine("  |                      |   ");
            legRight.AppendLine("  | __________________  /   ");
            legRight.AppendLine("  ||                  ||   ");
            legRight.AppendLine("  ||                  ||   ");
            legRight.AppendLine(@"  \\                  \\ ");

            board = legRight;
        }

        private void Bark()
        {
            StringBuilder bark = new StringBuilder();
            bark.AppendLine(" / __ \\             |\\___"); //use of escape keys
            bark.AppendLine(@" ||  |/             /    \___  //");
            bark.AppendLine(" ||                |       __|   BARK!");//use of literal
            bark.AppendLine(@" ||                |      /     \\");
            bark.AppendLine(@" \ \______________/      |  ");
            bark.AppendLine("  |                      |   ");
            bark.AppendLine("  | __________________  /   ");
            bark.AppendLine("  ||                  ||   ");
            bark.AppendLine("  ||                  ||   ");
            bark.AppendLine(@"  \\                  \\ ");

            board = bark;
        }
    }
}
