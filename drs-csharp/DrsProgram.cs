using System;
using System.Collections.Generic;

namespace drs_csharp
{
    public class DrsProgram
    {
        public void Initialize()
        {
            Console.WriteLine("A1: " + ValidateRent(new Rent(new DateTime(2020, 6, 20), new DateTime(2020, 6, 25))) + "\n");
            Console.WriteLine("A2: " + ValidateRent(new Rent(new DateTime(2020, 6, 26), new DateTime(2020, 6, 29))) + "\n");
            Console.WriteLine("A3: " + ValidateRent(new Rent(new DateTime(2020, 6, 29), new DateTime(2020, 7, 10))) + "\n");
            Console.WriteLine("A4: " + ValidateRent(new Rent(new DateTime(2020, 7, 20), new DateTime(2020, 7, 24))) + "\n");
            Console.WriteLine("A5: " + ValidateRent(new Rent(new DateTime(2020, 7, 20), new DateTime(2020, 7, 27))) + "\n");
            Console.WriteLine("A6: " + ValidateRent(new Rent(new DateTime(2020, 7, 27), new DateTime(2020, 8, 1))) + "\n");
            Console.WriteLine("A7: " + ValidateRent(new Rent(new DateTime(2020, 8, 15), new DateTime(2020, 8, 22))) + "\n");
            Console.WriteLine("A8: " + ValidateRent(new Rent(new DateTime(2020, 8, 20), new DateTime(2020, 9, 15))) + "\n");
        }

        private List<Rent> ReturnBookedDates()
        {
            return new List<Rent>
            {
                new Rent(new DateTime(2020, 6, 27), new DateTime(2020, 7, 15)),
                new Rent(new DateTime(2020, 7, 23), new DateTime(2020, 7, 26)),
                new Rent(new DateTime(2020, 8, 4), new DateTime(2020, 8, 19))
            };
        }

        private string AdjustDateFormat(DateTime date)
        {
            return date.ToString("dd.MM.yyyy");
        }

        private string ValidateRent(Rent rent)
        {
            List<Rent> bookedDates = ReturnBookedDates();
            int index = 0;
            foreach (Rent bookedDate in bookedDates)
            {
                if (rent.StartDate < bookedDate.EndDate && rent.EndDate > bookedDate.StartDate)
                {
                    return $"Rent between {AdjustDateFormat(rent.StartDate)} and {AdjustDateFormat(rent.EndDate)}" +
                        $" is not available due to {AdjustDateFormat(bookedDate.StartDate)} - {AdjustDateFormat(bookedDate.EndDate)}" +
                        $" reservation (R{index + 1})";
                }
                index++;
            }
            return $"Rent between {AdjustDateFormat(rent.StartDate)} and {AdjustDateFormat(rent.EndDate)} is available.";
        }
    }
}
