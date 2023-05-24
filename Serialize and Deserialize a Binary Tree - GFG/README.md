# Serialize and Deserialize a Binary Tree
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Serialization is to store a tree in an array&nbsp;so that it can be later restored and&nbsp;Deserialization is reading tree back from the array. Now your task is to complete the function<strong> serialize</strong> which stores the tree into an array A[ ] and <strong>deSerialize</strong> which deserializes&nbsp;the array to the tree and returns it.<br>
<strong>Note:&nbsp;</strong>The structure of the tree must be maintained. Multiple nodes can have the same data.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>&nbsp; &nbsp;&nbsp; &nbsp;1
 &nbsp; &nbsp;/&nbsp; &nbsp;\
 &nbsp;&nbsp;2&nbsp; &nbsp;&nbsp;&nbsp;3
<strong>Output: </strong>2 1 3</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;10
 &nbsp; &nbsp; &nbsp;&nbsp;/ &nbsp; &nbsp;\
 &nbsp; &nbsp;  20&nbsp; &nbsp; 30
 &nbsp;  /&nbsp;&nbsp; \
 &nbsp; 40&nbsp; 60
<strong>Output: </strong>40 20 60 10 30
</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
The task is to complete two&nbsp;functions<strong> serialize</strong> which takes the root node of the tree as input and stores the tree into an array&nbsp;and <strong>deSerialize</strong> which deserializes&nbsp;the array to the original tree and returns the root of it.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(N).<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(N).</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= Number of nodes &lt;= 1000<br>
1 &lt;= Data of a node &lt;= 1000</span></p>
</div>