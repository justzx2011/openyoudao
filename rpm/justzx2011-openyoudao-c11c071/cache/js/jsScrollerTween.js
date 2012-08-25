//Written by Nathan Faubion: http://n-son.com
//Use this or edit how you want, just give me
//some credit!

function jsScrollerTween (o, t, s) {
	var self = this;
	
	this._tweenTo = function (y) {
		if (self._idle) {
			var tHeight = self._parent._src ? self._parent._src.totalHeight : self._parent.totalHeight;
			var vHeight = self._parent._src ? self._parent._src.viewableHeight : self._parent.viewableHeight;
			var scrollY = self._parent._src ? self._parent._src._y : self._parent._y;
			
			if (y < 0) y = 0;
			if (y > tHeight - vHeight) y = tHeight - vHeight;
			
			var dist = y - (-scrollY);
			
			self._inc = 0;
			self._timer = null;
			self._values = [];
			self._idle = false;
			for (var i = 0; i < self.steps.length; i++) {
				self._values[i] = Math.round((-scrollY) + dist * (self.steps[i] / 100));
			}
			self._timer = window.setInterval(function () {
				self._parent.scrollTo(0, self._values[self._inc]);
				if (self._inc == self.steps.length-1) {
					window.clearTimeout(self._timer);
					self._idle = true;
				} else self._inc++;
			}, self.stepDelay);
		}
	};
	this._tweenBy = function (y) {
		var scrollY = self._parent._src ? self._parent._src._y : self._parent._y;
		self._tweenTo(-scrollY + y);
	};
	this._trackTween = function (e) {
		e = e ? e : event;
		self._parent.canScroll = false;
		var curY = e.clientY + document.body.scrollTop;
		self._tweenTo((curY - self._parent._trackTop - self._parent._handleHeight/2) * self._parent._ratio);
	};
	
	this.stepDelay = 40;
	this.steps   = s?s:[0,25,50,70,85,95,97,99,100];
	this._values = [];
	this._parent = o;
	this._timer  = [];
	this._idle   = true;
	
	o.tweenTo = this._tweenTo;
	o.tweenBy = this._tweenBy;
	o.trackTween = this._trackTween;
	
	if (t) o._scrollTrack = function (e) {
		this.trackTween(e);
	};
};