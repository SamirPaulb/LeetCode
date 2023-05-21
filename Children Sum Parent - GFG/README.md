# Children Sum Parent
## Easy
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a Binary Tree. Check whether all of its nodes have the value equal to the sum of their child nodes.</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>     10
    /
  10 
<strong>Output: </strong>1<strong>
Explanation: </strong>Here, every node is sum of
its left and right child.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>       1
     /   \
&nbsp;   4     3
&nbsp;  /  \
&nbsp; 5    N
<strong>Output: </strong>0<strong>
Explanation: </strong>Here, 1 is the root node
and 4, 3 are its child&nbsp;nodes. 4 + 3 =
7 which is not equal to the value of
root node. Hence, this tree does not
satisfy the given conditions.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function</span><span style="font-size:18px"> <strong>isSumProperty</strong>() that takes the root Node of the Binary Tree as input and returns 1 if all the nodes in the tree satisfy the following properties. Else, it returns 0.<br>
For every node, data value must be equal to the&nbsp;sum of data values in left and right children. Consider data value as 0 for NULL child.&nbsp; Also, leaves are considered to follow the property.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexiy:&nbsp;</strong>O(N).<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(Height of the Tree).</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N &lt;= 10<sup>5</sup><br>
1 &lt;= Data on nodes &lt;= 10<sup>5</sup></span></p>
</div>