'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://gist.github.com/hariketsheth/7298d48c175a4111d960a2f27df14c53"


#  Mod:
#  - replaced has_key() with "in".


"""
I Love Lance & Janice
=====================

You've caught two of your fellow minions passing coded notes back and forth -- while they're on duty, no less! Worse, you're pretty sure it's not job-related -- they're both huge fans of the space soap opera ""Lance & Janice"". You know how much Commander Lambda hates waste, so if you can prove that these minions are wasting time passing non-job-related notes, it'll put you that much closer to a promotion. 

Fortunately for you, the minions aren't exactly advanced cryptographers. In their code, every lowercase letter [a..z] is replaced with the corresponding one in [z..a], while every other character (including uppercase letters and punctuation) is left untouched.  That is, 'a' becomes 'z', 'b' becomes 'y', 'c' becomes 'x', etc.  For instance, the word ""vmxibkgrlm"", when decoded, would become ""encryption"".

Write a function called solution(s) which takes in a string and returns the deciphered string so you can show the commander proof that these minions are talking about ""Lance & Janice"" instead of doing their jobs.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
Output:
    did you see last night's episode?

Input:
solution.solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
Output:
    Yeah! I can't believe Lance lost his job at the colony!!

-- Java cases --
Input:
Solution.solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
Output:
    Yeah! I can't believe Lance lost his job at the colony!!

Input:
Solution.solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
Output:
    did you see last night's episode?
"""

def solution(s):
	norm = [i for i in range(97, 123)]
	rev = [j for j in range(122, 96, -1)]
	dict_sent = {norm[n]: rev[n] for n in range(len(norm))}

	decrypted = []

	for c in s:
		#f dict_sent.has_key(ord(c)):
		if ord(c) in dict_sent:
			decrypted.append(chr(dict_sent[ord(c)]))
		else:
			decrypted.append(c)

	return ''.join(decrypted)

