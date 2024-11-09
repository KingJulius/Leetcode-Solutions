/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
    let isThrottled = false;
    let nextArgs;
    return function(...args) {
        if (isThrottled){
            // If throttled --> Saves arguments
            nextArgs = args;
        } else {
            fn(...args);
            isThrottled = true;
            setTimeout(helper, t);
        }

        function helper() {
            if (nextArgs){
                fn(...nextArgs);
                isThrottled = true;
                nextArgs = null;
                setTimeout(helper, t);

            } else {
                // Clears Throttle once timer has passed
                isThrottled = false;
            }
        }
    }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */