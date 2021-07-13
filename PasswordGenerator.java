import java.util.Random;

public class PasswordGenerator 
{

	public static void main(String[] args) 
	{		
		int length = 12;
		System.out.print(generatePass(length));
	}
	static char[] generatePass(int len)
	{
		System.out.println("Your Password Is : ");
		String UprChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		String LwrChar = "abcdefghijklmnopqrstuvwxyz";
		String numbers = "0123456789";
		String symbols="!@#$&*_-.";
		String pass = UprChar+symbols+LwrChar+numbers;
		Random rnd = new Random();
		char[] password = new char[len];
		for (int i = 0; i < password.length; i++) 
		{
			password[i] = pass.charAt(rnd.nextInt(pass.length()));
		}
		return password;
	}
	
}
