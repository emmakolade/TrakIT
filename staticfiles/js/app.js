!(function (e, n) {
  "object" == typeof exports && "object" == typeof module
    ? (module.exports = n())
    : "function" == typeof define && define.amd
    ? define("smart-app", [], n)
    : "object" == typeof exports
    ? (exports["smart-app"] = n())
    : (e["smart-app"] = n());
})(window, function () {
  return (function (e) {
    function n(n) {
      for (
        var r, u, a = n[0], p = n[1], c = n[2], l = 0, s = [];
        l < a.length;
        l++
      )
        (u = a[l]), o[u] && s.push(o[u][0]), (o[u] = 0);
      for (r in p) Object.prototype.hasOwnProperty.call(p, r) && (e[r] = p[r]);
      for (f && f(n); s.length; ) s.shift()();
      return i.push.apply(i, c || []), t();
    }
    function t() {
      for (var e, n = 0; n < i.length; n++) {
        for (var t = i[n], r = !0, a = 1; a < t.length; a++) {
          var p = t[a];
          0 !== o[p] && (r = !1);
        }
        r && (i.splice(n--, 1), (e = u((u.s = t[0]))));
      }
      return e;
    }
    var r = {},
      o = { 0: 0 },
      i = [];
    function u(n) {
      if (r[n]) return r[n].exports;
      var t = (r[n] = { i: n, l: !1, exports: {} });
      return e[n].call(t.exports, t, t.exports, u), (t.l = !0), t.exports;
    }
    (u.m = e),
      (u.c = r),
      (u.d = function (e, n, t) {
        u.o(e, n) || Object.defineProperty(e, n, { enumerable: !0, get: t });
      }),
      (u.r = function (e) {
        "undefined" != typeof Symbol &&
          Symbol.toStringTag &&
          Object.defineProperty(e, Symbol.toStringTag, { value: "Module" }),
          Object.defineProperty(e, "__esModule", { value: !0 });
      }),
      (u.t = function (e, n) {
        if ((1 & n && (e = u(e)), 8 & n)) return e;
        if (4 & n && "object" == typeof e && e && e.__esModule) return e;
        var t = Object.create(null);
        if (
          (u.r(t),
          Object.defineProperty(t, "default", { enumerable: !0, value: e }),
          2 & n && "string" != typeof e)
        )
          for (var r in e)
            u.d(
              t,
              r,
              function (n) {
                return e[n];
              }.bind(null, r)
            );
        return t;
      }),
      (u.n = function (e) {
        var n =
          e && e.__esModule
            ? function () {
                return e.default;
              }
            : function () {
                return e;
              };
        return u.d(n, "a", n), n;
      }),
      (u.o = function (e, n) {
        return Object.prototype.hasOwnProperty.call(e, n);
      }),
      (u.p = "");
    var a = (window.webpackJsonpsmart_app = window.webpackJsonpsmart_app || []),
      p = a.push.bind(a);
    (a.push = n), (a = a.slice());
    for (var c = 0; c < a.length; c++) n(a[c]);
    var f = p;
    return i.push([0, 2]), t();
  })([
    function (e, n, t) {
      var r = t(1),
        o = t(2),
        i = (function () {
          var e = {};
          function n() {
            r("body").hasClass("nav-open")
              ? r("body").removeClass("nav-open")
              : r("body").addClass("nav-open");
          }
          return (
            (e.init = function () {
              r("#navOpener").on("click", n),
                console.log("Smart App Initialized Successfully..:-) "),
                o.init();
            }),
            e
          );
        })();
      !(function (e) {
        "interactive" === document.readyState ||
        "complete" === document.readyState
          ? e()
          : document.addEventListener("DOMContentLoaded", e);
      })(function () {
        i.init();
      });
    },
    ,
    function (e, n, t) {
      var r = t(3),
        o = (function () {
          return {
            init: function () {
              new r.Line(
                "#incomeExpenseChart",
                {
                  labels: ["Jun", "Jul", "Aug", "Sep", "Dec"],
                  series: [
                    [0, 4e3, 6e3, 3e3, 4e3, 8e3, 6e3],
                    [0, 1e3, 1500, 4e3, 3e3, 6e3, 4e3],
                  ],
                },
                { fullWidth: !0, height: "250px", chartPadding: { right: 40 } }
              );
            },
          };
        })();
      e.exports = o;
    },
  ]);
});
