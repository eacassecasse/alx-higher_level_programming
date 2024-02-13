#!/usr/bin/node

exports.esrever = function (list) {
    return list.map((el, index, array) => {
        return array[array.length - 1 - index];
    })
}