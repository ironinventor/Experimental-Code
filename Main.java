package com.github.ironinventor;

public class Main {

	public static void main(String[] args) {
		//Basic print statement in java
		System.out.println("Hello World!");
		System.out.println("Println separates print statements in console");
		System.out.print("Hello ");
        System.out.print("World!-");
        System.out.println(" ");
        
        //Variable declaration in java basics
        int x = 5;
        double y = 5.5;
        //Basic conditionals
        if(x != 5) {
        	System.out.println("x does not equal to 5");
        	
        }else {
        	System.out.println("x does = 5");
        }
        //Like wise we can do the same with double
        /* This
         * is 
         * a
         * multiline
         * 
         * comment
         */
        //Now we will define a standard for loop for looping your code
        
        for(int i=1; i<11; i++){
        	System.out.println("count is " + i);
        	
        	
        }
        //now looping characters
        char a='A';
        
       for(int i=0;i<26;i++)
       {
           System.out.println(a);
           a++;
       }

        
	}

}
