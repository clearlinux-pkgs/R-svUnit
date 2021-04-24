#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-svUnit
Version  : 1.0.6
Release  : 23
URL      : https://cran.r-project.org/src/contrib/svUnit_1.0.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/svUnit_1.0.6.tar.gz
Summary  : 'SciViews' - Unit, Integration and System Testing
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n svUnit
cd %{_builddir}/svUnit

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618846755

%install
export SOURCE_DATE_EPOCH=1618846755
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library svUnit
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library svUnit
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library svUnit
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc svUnit || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/svUnit/CITATION
/usr/lib64/R/library/svUnit/DESCRIPTION
/usr/lib64/R/library/svUnit/INDEX
/usr/lib64/R/library/svUnit/Meta/Rd.rds
/usr/lib64/R/library/svUnit/Meta/features.rds
/usr/lib64/R/library/svUnit/Meta/hsearch.rds
/usr/lib64/R/library/svUnit/Meta/links.rds
/usr/lib64/R/library/svUnit/Meta/nsInfo.rds
/usr/lib64/R/library/svUnit/Meta/package.rds
/usr/lib64/R/library/svUnit/Meta/vignette.rds
/usr/lib64/R/library/svUnit/NAMESPACE
/usr/lib64/R/library/svUnit/NEWS.md
/usr/lib64/R/library/svUnit/R/svUnit
/usr/lib64/R/library/svUnit/R/svUnit.rdb
/usr/lib64/R/library/svUnit/R/svUnit.rdx
/usr/lib64/R/library/svUnit/TestsvUnit.R
/usr/lib64/R/library/svUnit/WORDLIST
/usr/lib64/R/library/svUnit/doc/index.html
/usr/lib64/R/library/svUnit/doc/svUnit.R
/usr/lib64/R/library/svUnit/doc/svUnit.Rmd
/usr/lib64/R/library/svUnit/doc/svUnit.html
/usr/lib64/R/library/svUnit/help/AnIndex
/usr/lib64/R/library/svUnit/help/aliases.rds
/usr/lib64/R/library/svUnit/help/paths.rds
/usr/lib64/R/library/svUnit/help/svUnit.rdb
/usr/lib64/R/library/svUnit/help/svUnit.rdx
/usr/lib64/R/library/svUnit/html/00Index.html
/usr/lib64/R/library/svUnit/html/R.css
/usr/lib64/R/library/svUnit/komodo/sciviewskunit-ko.xpi
/usr/lib64/R/library/svUnit/tests/spelling.R
/usr/lib64/R/library/svUnit/tests/test-with-svUnit.R
/usr/lib64/R/library/svUnit/tests/testthat/test.svUnit.R
/usr/lib64/R/library/svUnit/unitTests/BadTests/runitBadTests.R
/usr/lib64/R/library/svUnit/unitTests/VirtualClass/runitVirtualClass.R
/usr/lib64/R/library/svUnit/unitTests/runitsvSuite.R
/usr/lib64/R/library/svUnit/unitTests/runitsvTest.R
