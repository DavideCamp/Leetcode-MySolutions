/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {

    const map = new Map();
    return function(...args) {
        let parameters = JSON.stringify(args)
        if(!map.has(parameters)) {
           map.set(parameters, fn(...args));
        } 
        return map.get(parameters)
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */