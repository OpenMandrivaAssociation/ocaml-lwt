Name:           ocaml-lwt
Version:        2.1.1
Release:        %mkrel 1
Summary:        Cooperative light-weight thread library for OCaml
Group:          Development/Other
License:        LGPLv2+ with exceptions
URL:            http://ocsigen.org/lwt/
Source0:        http://ocsigen.org/download/lwt-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml-findlib
BuildRequires:  camlp4
BuildRequires:  ocaml-ssl >= 0.4.0
BuildRequires:  ocaml-react
BuildRequires:  ocaml-lablgtk2
Requires:  ocaml-react
Requires:  ocaml-lablgtk2

%description
Lwt is a lightweight thread library for Objective Caml.
This library of cooperative threads is implemented in monadic style.
With respect to preemptive threads, cooperative threads are not using a
scheduler to distribute processor time between threads. Instead of this,
each thread must tell the others that he wants to let them work.
This library is part of the Ocsigen project.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n lwt-%{version}

mv README README.old
iconv -f iso-8859-1 -t utf-8 < README.old > README

%build
make
make doc

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE COPYING
%dir %{_libdir}/ocaml/lwt
%{_libdir}/ocaml/lwt/META
%{_libdir}/ocaml/lwt/*.cma
%{_libdir}/ocaml/lwt/*.cmi

%files devel
%defattr(-,root,root)
%doc LICENSE COPYING CHANGES CHANGES.darcs README VERSION _build/lwt.docdir
%{_libdir}/ocaml/lwt/*.a
%{_libdir}/ocaml/lwt/*.cmxa
%{_libdir}/ocaml/lwt/*.cmx
%{_libdir}/ocaml/lwt/*.mli
%{_libdir}/ocaml/lwt/*.cmo
%{_libdir}/ocaml/stublibs/*.so*

