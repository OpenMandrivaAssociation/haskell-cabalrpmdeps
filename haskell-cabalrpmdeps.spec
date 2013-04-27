%define module cabalrpmdeps
%define _no_haddock 0

Name: haskell-%{module}
Version: 0.0.4
Release: 13
Summary: Tools to build rpm dependencies from Cabal
Group: Development/Other
License: LGPL
url: http://hackage.haskell.org/package/%{module}
source0: http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
# actualize code for ghc-7.6.1
# thanks to Roman Cheplyaka:
# https://groups.google.com/group/haskell-russian/browse_thread/thread/507bf0121ecebe60
patch0: cabalrpmdeps-0.0.4.nohaskell98.patch
BuildRequires: ghc
BuildRequires: ghc-devel
buildrequires: haskell-macros
requires:      haddock
requires(post): haddock
requires(preun): haddock

%description
Tools to build rpm dependencies from Cabal

%package -n %{module}
Summary: Tools to build rpm dependencies from Cabal
Group: Development/Other
requires: ghc
requires(post): ghc
requires(preun): ghc

%description -n %{module}
Tools to build rpm dependencies from Cabal

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1 -b .nohaskell98

%build
%_cabal_build

%check
%_cabal_check

%install
%_cabal_install

%_cabal_rpm_gen_deps

%_cabal_scriptlets

%files
%defattr(-,root,root)
%doc %{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}

%files -n %{module}
%defattr(-,root,root)
%_cabal_rpm_deps_dir
%_bindir/*




%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.4-5mdv2011.0
+ Revision: 611058
- rebuild

* Wed Feb 10 2010 Funda Wang <fwang@mandriva.org> 0.0.4-4mdv2010.1
+ Revision: 503650
- rebuild

* Sun Nov 08 2009 Olivier Thauvin <nanardon@mandriva.org> 0.0.4-3mdv2010.1
+ Revision: 463198
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Dec 04 2008 Olivier Thauvin <nanardon@mandriva.org> 0.0.4-1mdv2009.1
+ Revision: 309891
- 0.0.4 (new ghc)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Thu Mar 15 2007 Olivier Thauvin <nanardon@mandriva.org> 0.0.3-2mdv2007.1
+ Revision: 143912
- add provide
- 0.0.3

* Sat Mar 10 2007 Olivier Thauvin <nanardon@mandriva.org> 0.0.2-1mdv2007.1
+ Revision: 140870
- Import haskell-cabalrpmdeps

