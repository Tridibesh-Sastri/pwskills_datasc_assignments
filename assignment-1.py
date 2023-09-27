{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9438378e-7c9d-4655-a8b3-c01f5e8937fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c5e472bc-eded-46af-b2a1-3f30a300cbf3",
   "metadata": {},
   "outputs": [],
   "source": [
    "#i) String\n",
    "s = \"Pwskills\"\n",
    "\n",
    "#ii) list\n",
    "l = [1,3,s, 'r',3+5j,3.33344]\n",
    "\n",
    "#ii) float\n",
    "f = 3.23425\n",
    "\n",
    "#iv) tuple\n",
    "t = (1,3,s,l,f,3+7j)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6a5f9c75-7b19-4892-bfae-9c6b1de4734f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6ddce301-b0b5-4206-8055-d049c8966a49",
   "metadata": {},
   "outputs": [],
   "source": [
    "#i) string\n",
    "var1 = ''\n",
    "\n",
    "#ii) string \n",
    "var2 = '[DS, ML, Python]'\n",
    "\n",
    "#iii) list\n",
    "var3 = ['DS', 'ML', 'Python']\n",
    "\n",
    "#iv) int\n",
    "var4 = 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "610ab5f0-e6b1-443e-a72a-7c83c6bc0411",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "1d103a97-a51d-47ad-80e2-f2522c373ad0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4.5"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#i) '/' gives quotient of division\n",
    "9/2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "eff7de44-49b3-4b56-9d90-fc5764160f2b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#ii) '%' gives remainder of division\n",
    "9%2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "213e3fe4-79d9-4cf7-8aec-1732b46f0029",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#iii) '//' gives integer value of quotient of division\n",
    "9//2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e7b693ab-5cb2-4b48-9c09-add81ca1600f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "81"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#iv) '**' implies the power of a number here 2 is the power of 9\n",
    "9**2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "53bc259d-6f74-4b37-bdee-1459bacdc24d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b2cff19c-845c-41fb-b18f-52095a884276",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2<class 'int'>\n",
      "3<class 'int'>\n",
      "Pwskills<class 'str'>\n",
      "r<class 'str'>\n",
      "(3+5j)<class 'complex'>\n",
      "3.33344<class 'float'>\n",
      "Gopal<class 'str'>\n",
      "True<class 'bool'>\n",
      "{1, (3+5j), 3.33344, 'Gopal'}<class 'set'>\n",
      "((3+5j), 3.33344, 'Gopal', True)<class 'tuple'>\n"
     ]
    }
   ],
   "source": [
    "l1 = [2,3,s, 'r',3+5j,3.33344,\"Gopal\",True,{1,3+5j,3.33344,\"Gopal\",True},(3+5j,3.33344,\"Gopal\",True)]\n",
    "for i in l1:\n",
    "    print(str(i) + str(type(i)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "a6cae38c-235d-4c19-b606-e37b92b97664",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Questioon 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "59410a03-4ba5-4c6d-836b-f9bda2c1cf86",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter num 1\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 99\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter num 2\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A is not divisible by B\n",
      "A is divisible B and it can divisible by 2 times\n"
     ]
    }
   ],
   "source": [
    "print('Enter num 1')\n",
    "a = int(input())\n",
    "print('Enter num 2')\n",
    "b = int(input())\n",
    "\n",
    "n = a\n",
    "times = 0\n",
    "\n",
    "while n >= b:\n",
    "\n",
    "    if n % b == 0:\n",
    "        times = times + 1\n",
    "        n = n / b\n",
    "    else :\n",
    "        print(\"A is not divisible by B\")\n",
    "        break\n",
    "    \n",
    "if times > 0:\n",
    "    print(\"A is divisible B and it can divisible by \" + str(times) + \" times\")\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6538e745-bb88-4aac-85ea-7785351fa138",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Questioon 6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "131b9bca-8d2d-4fe2-acb4-0967f3ea8417",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 is not divisible by 3\n",
      "2 is not divisible by 3\n",
      "3 is divisible by 3\n",
      "4 is not divisible by 3\n",
      "5 is not divisible by 3\n",
      "6 is divisible by 3\n",
      "7 is not divisible by 3\n",
      "8 is not divisible by 3\n",
      "9 is divisible by 3\n",
      "0 is divisible by 3\n",
      "12 is divisible by 3\n",
      "13 is not divisible by 3\n",
      "14 is not divisible by 3\n",
      "15 is divisible by 3\n",
      "16 is not divisible by 3\n",
      "17 is not divisible by 3\n",
      "18 is divisible by 3\n",
      "19 is not divisible by 3\n",
      "20 is not divisible by 3\n",
      "21 is divisible by 3\n",
      "22 is not divisible by 3\n",
      "25 is not divisible by 3\n",
      "23 is not divisible by 3\n",
      "24 is divisible by 3\n"
     ]
    }
   ],
   "source": [
    "l2 = [1,2,3,4,5,6,7,8,9,0,12,13,14,15,16,17,18,19,20,21,22,25,23,24]\n",
    "\n",
    "for i in l2:\n",
    "    if i % 3 == 0:\n",
    "        print(str(i) + \" is divisible by 3\" )\n",
    "    else:\n",
    "        print(str(i) + \" is not divisible by 3\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "765eff0b-2223-48ee-8aa9-b87ad55b3dca",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'str' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[36], line 11\u001b[0m\n\u001b[1;32m      8\u001b[0m l[\u001b[38;5;241m0\u001b[39m] \u001b[38;5;241m=\u001b[39m s[\u001b[38;5;241m0\u001b[39m]\n\u001b[1;32m      9\u001b[0m l[\u001b[38;5;241m0\u001b[39m]\n\u001b[0;32m---> 11\u001b[0m \u001b[43ms\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;241;43m1\u001b[39;49m\u001b[43m]\u001b[49m \u001b[38;5;241m=\u001b[39m l[\u001b[38;5;241m1\u001b[39m]\n",
      "\u001b[0;31mTypeError\u001b[0m: 'str' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "# Question 6\n",
    "\"\"\"In which data type we can modify value in any index these dats types are known as mutable data\n",
    "and for which we can't modify is known as immutable dsta\"\"\"\n",
    "\n",
    "#mutable data\n",
    "l = [1,3,6]\n",
    "s = \"gopal\"\n",
    "l[0] = s[0]\n",
    "l[0]\n",
    "\n",
    "# s[1] = l[1] this action is not possible"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1280e111-d01a-4914-b361-1c0a14ed6c17",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
