package com.sap;

import org.junit.Test;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.is;

//https://www.hackerrank.com/challenges/reduced-string/

public class SuperReducedString {

    static String superReducedString(String s) {
        return s;
    }

    @Test
    public void testA() {
        assertThat(superReducedString("aaabccddd"), is("abd"));
    }

    @Test
    public void testB() {
        assertThat(superReducedString("aa"), is(""));
    }

    @Test
    public void testC() {
        assertThat(superReducedString("baab"), is(""));
    }


    @Test
    public void testD() {
        assertThat(superReducedString("ppffccmmssnnhhbbmmggxxaaooeeqqeennffzzaaeeyyaaggggeessvvssggbbccnnrrjjxxuuzzbbjjrruuaaccaaoommkkkkxx"), is(""));
    }
}

