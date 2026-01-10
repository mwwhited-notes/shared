using System.Linq;
using System.Text;

namespace RadexOne.Decoder
{
    public static class ToolsEx
    {
        public static decimal ToNumber(this byte[] buffer, int offset, decimal mag = 1m) =>
             (
                 buffer[offset] +
                 (buffer[offset + 1] << 8) +
                 (buffer[offset + 2] << 16) +
                 (buffer[offset + 3] << 24)
             ) / mag;
        public static ushort ToUShort(this byte[] buffer, int offset) =>
             (ushort)(
                 buffer[offset] +
                 (buffer[offset + 1] << 8)
             );

        public static string ToHexString(this byte[] buffer, int length) =>
             buffer.Take(length)
                   .Aggregate(new StringBuilder(), (sb, v) => sb.Append(v.ToString("X2")))
                   .ToString();
    }
}

// SN: 180620-0840-008344 v1.8
// 7AFF 2080 1E00 B100 ____ 957F _100 ____ 1400 ____ 11A4 ____ 9820 ____ 1400 _612 _108 4803 _800 ____ D61D
//                                                            8344                     0840
