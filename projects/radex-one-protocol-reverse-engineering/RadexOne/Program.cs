using System;
using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;

namespace RadexOne
{
    class Program
    {
        static void Main(string[] args)
        {
            var file = "RADEXOne-2020.09.21-20.33.csv";
            var result = "radexone_out.csv";
            //"No.,Time,Source,Destination,Protocol,Length,Info,capture"

            var decoded = Decode(file);


            var aligned = from d in decoded
                          let rowkey = d.data.Substring(12, 4)
                          let rowId = ToNumber(rowkey)
                          group d by rowId into g
                          select new
                          {
                              Row = g.Key,
                              Output = Split(g.FirstOrDefault(i => i.direction == "O").data),
                              Input = Split(g.FirstOrDefault(i => i.direction == "I").data),
                          };

            var clean = from d in aligned
                        select new
                        {
                            d.Row,
                            d.Output,
                            d.Input,

                            //OutputUInt16s = string.Join(' ', d.Output.Split(' ').Select(b => Convert.ToUInt16(b == "" ? "ffff" : b, 16)).Select(u => u == 0 ? "____" : u.ToString("X2").PadLeft(4, '_'))),
                            //InputUInt16s = string.Join(' ', d.Input.Split(' ').Select(b => Convert.ToUInt16(b, 16)).Select(u => u == 0 ? "____" : u.ToString("X2").PadLeft(4, '_'))),

                            //OutputUInt16N = string.Join(' ', d.Output.Split(' ').Select(b => ToNumber(b == "" ? "ffff" : b)).Select(u => u == 0 ? "____" : u.ToString("X2").PadLeft(4, '_'))),
                            //InputUInt16N = string.Join(' ', d.Input.Split(' ').Select(b => ToNumber(b)).Select(u => u == 0 ? "____" : u.ToString("X2").PadLeft(4, '_'))),

                            //OutputUInt16D = string.Join(' ', d.Output.Split(' ').Select(b => ToNumber(b == "" ? "ffff" : b)).Select(u => u == 0 ? "____" : u.ToString().PadLeft(5, '_'))),
                            //InputUInt16D = string.Join(' ', d.Input.Split(' ').Select(b => ToNumber(b)).Select(u => u == 0 ? "____" : u.ToString().PadLeft(5, '_'))),
                        };



            //var x = from e in decoded
            //        where e.Output.Length == 36
            //        let len = Math.Min(e.Output.Length, e.Output.Length)
            //        //let output = e.Output.Substring(0, len)
            //        //let input = e.Input.Substring(0, len)
            //        //let matched = new string(
            //        //    output.Select((c, i) => (char)c % input.ElementAt(i))
            //        //    .Select(c => (char)(c == 0 ? '_' : c))
            //        //    .ToArray()
            //        //    )
            //        select new
            //        {
            //            e,
            //            matched,
            //        };

            // File.WriteAllLines(result, clean.Select(d => string.Join(',', d.Row, d.OutputUInt16N, d.InputUInt16N, d.OutputUInt16D, d.InputUInt16D)));
            File.WriteAllLines(result, clean.Select(d => string.Join(',', d.Row, d.Output, d.Input)));
        }

        private static int ToNumber(string input) => int.Parse(input.Substring(2, 2) + input.Substring(0, 2), NumberStyles.HexNumber);

        private static string Split(string input, int cnt = 4, char del = ' ') =>
            string.Join(del,
               (input ?? "").Select((c, i) => (c, o: i % cnt, k: i / cnt))
                     .GroupBy(g => g.k)
                     .Select(g => new string(g.OrderBy(i => i.o).Select(i => i.c).ToArray()))
                );

        private static IEnumerable<(string direction, string data)> Decode(string file)
        {
            var decoded = from line in File.ReadAllLines(file).Skip(1)
                          let parts = line.Replace("\"", "").Split(',')
                          select new
                          {
                              Number = parts.ElementAtOrDefault(0),
                              Time = parts.ElementAtOrDefault(1),
                              Source = parts.ElementAtOrDefault(2),
                              Destination = parts.ElementAtOrDefault(3),
                              Protocol = parts.ElementAtOrDefault(4),
                              Length = parts.ElementAtOrDefault(5),
                              Info = parts.ElementAtOrDefault(6),
                              Capture = parts.ElementAtOrDefault(7),
                          };

            var filtered = from d in decoded
                           where (d.Source == "host" && d.Info == "URB_BULK out") ||
                                 (d.Source == "1.9.1" && d.Info == "URB_BULK in")
                           select d;

            var output = false;
            var last = output;
            var sb = new StringBuilder();
            foreach (var d in filtered)
            {
                output = d.Info == "URB_BULK out";
                if (output != last)
                {
                    if (sb.Length > 0)
                        yield return (last ? "O" : "I", sb.ToString());
                    sb.Clear();
                }

                sb.Append(d.Capture);

                last = output;
            }

            if (sb.Length > 0)
                yield return (last ? "O" : "I", sb.ToString());
        }
    }
}
