using System;

namespace drs_csharp
{
    public class Rent
    {
        public DateTime StartDate;

        public DateTime EndDate;

        public Rent(DateTime startDate, DateTime endDate)
        {
            StartDate = startDate;
            EndDate = endDate;
        }
    }
}
