using System;
namespace LightCalc
{
    class Program
    {
        static void Main(string[] args)
        {
        top:
            var lux = ConsoleEx.Prompt("Lux").ToDouble();
            var iso = ConsoleEx.Prompt("ISO").ToDouble();
            var aperture = ConsoleEx.Prompt(("f/Stop")).ToDouble();
            var shutter = ConsoleEx.Prompt("Shutter Speed").ToDouble();
            if (!lux.HasValue && !iso.HasValue && !aperture.HasValue && !shutter.HasValue)
            {
                return;
            }
            else if (!lux.HasValue)
            {
                // (POWER(A, 2) * 250) / (I * S)
                lux = (Math.Pow(aperture ?? 0d, 2d) * 250d) / ((iso ?? 0d) * (shutter ?? 0d));
            }
            else if (!iso.HasValue)
            {
                // (POWER(A,2)*250)/(L*S)
                iso = (Math.Pow(aperture ?? 0d, 2d) * 250d) / ((lux ?? 0d) * (shutter ?? 0d));
            }
            else if (!aperture.HasValue)
            {
                // SQRT(L*S/2.5*I/100)
                aperture = Math.Sqrt((lux ?? 0d) * (shutter ?? 0d) / 2.5d * (iso ?? 0d) / 100);
            }
            else if (!shutter.HasValue)
            {
                // POWER(A,2)*2.5/L*100/I
                shutter = Math.Pow(aperture ?? 0d, 2d) * 2.5 / (lux ?? 0d) * 100 / (iso ?? 0d);
            }
            // LOG(L/2.5,2)
            var reqEv = Math.Log((lux ?? 0d) / 2.5d, 2d);

            // LOG(POWER(A,2)/S,2)
            var actEv = Math.Log(Math.Pow((aperture ?? 0d), 2d) / (shutter ?? 0d), 2d);

            Console.WriteLine("Lux: {0}", lux);
            Console.WriteLine("ISO: {0}", iso);
            Console.WriteLine("f/Stop {0}", aperture);
            Console.WriteLine("Shutter: {0} ({1})", shutter, shutter < 1 ? string.Format("1/{0}", 1d / shutter) : string.Format("{0}", shutter));
            Console.WriteLine("E: {0}\r\nA: {1}", reqEv, actEv);

            goto top;
        }
    }
}


Using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace LightCalc
{
    public static class NumberEx
    {
        public static float? ToFloat(this string input)
        {
            float ret;
            if (float.TryParse(input, out ret))
                return ret;
            return null;
        }
        public static int? ToInteger(this string input)
        {
            int ret;
            if (int.TryParse(input, out ret))
                return ret;
            return null;
        }
        public static decimal? ToDecimal(this string input)
        {
            decimal ret;
            if (decimal.TryParse(input, out ret))
                return ret;
            return null;
        }
        public static double? ToDouble(this string input)
        {
            double ret;
            if (double.TryParse(input, out ret))
                return ret;
            else if (input?.Trim().StartsWith("1/") ?? false)
                if (double.TryParse(input.Trim().Substring(2), out ret))
                    return 1d / ret;
            return null;
        }
    }
}


