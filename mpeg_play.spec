Summary:	Berkeley MPEG-1 Video Decoder
Summary(pl):	Dekoder obrazu MPEG-1 z Berkeley
Name:		mpeg_play
Version:	2.4
Release:	3
License:	BSD
Group:		X11/Applications/Multimedia
Source0:	ftp://mm-ftp.cs.berkeley.edu/pub/mpeg/play/%{name}-%{version}-src.tar.gz
# Source0-md5:	4e56f1d436639e79c3d0f49857510361
URL:		ftp://mm-ftp.cs.berkeley.edu/pub/mpeg/
Patch0:		%{name}-morearchs.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The decoder is implemented as a library that will take a video stream
and display it in an X window on an 8, 24 or 32 bit deep display. The
main routine is supplied to demonstrate the use of the decoder
library. Several dithering algorithms are supplied based on the
Floyd-Steinberg, ordered dither, and half-toning algorithms that
tradeoff quality and performance. Neither the library nor the main
routine handle real-time synchronization or audio streams.

%description -l pl
Dekoder jest zaimplementowany jako biblioteka przetwarzaj±ca strumieñ
MPEG-1 i wy¶wietlaj±ca go w okienku X Window w 8, 24 lub 32 bpp.
Obs³uguje kilka rodzajów ditheringu (Floyd-Steinberg, ordered dither,
half-toning), nie obs³uguje natomiast synchronizacji ani strumieni
audio.

%prep
%setup -q -c
%patch0 -p1

%build
%{__make} -C mpeg_play -fMakefile.proto \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/X11R6/include" \
	LDFLAGS="%{rpmldflags} -L/usr/X11R6/%{_lib}" \
	LIBS="-lX11 -lXext"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install mpeg_play/mpeg_play.1 $RPM_BUILD_ROOT%{_mandir}/man1
install mpeg_play/mpeg_play $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc mpeg_play/{ANNOUNCE,BUGS,CHANGES,PLATFORMS,README*,TODO,VERSION}
%attr(755,root,root) %{_bindir}/mpeg_play
%{_mandir}/man1/mpeg_play.1*
