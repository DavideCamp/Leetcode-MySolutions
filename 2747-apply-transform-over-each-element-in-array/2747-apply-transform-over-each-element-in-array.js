/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    res = []
    arr.forEach((n, i) => res.push(fn(n, i)));
    return res
};