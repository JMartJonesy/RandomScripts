public class reverseString
{
public static String reverse( String s )
{
	char[] chars = s.toCharArray();

	for(int i = 0; i < chars.length/2; i++)
	{
		char swapChar = chars[i];
		chars[i] = chars[((chars.length)-1) - i];
		chars[((chars.length)-1) - i] = swapChar;
	}

	return new String(chars);
}

public static void main(String[] args)
{
	System.out.println(reverse(args[0]));
}
}
