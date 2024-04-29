from SA import SuffixArray
from TestingUtils import generate_test_cases

if __name__ == '__main__':
    sas = []
    passed = 0
    failed = 0
    tests = generate_test_cases(10,10,10)
    tests += generate_test_cases(10,10,10)
    tests += generate_test_cases(10,10,10)
    for test in tests:
        sa = SuffixArray(test['text'])
        sas.append(sa)
        plcp = sa.getPLCP()
        encodedPLCP = sa.getEncodedPLCP()
        lcp = sa.construct_lcp_normal(plcp)
        lcpFromEncoded = sa.construct_lcp_from_encoded_plcp(encodedPLCP)
        if sa.ranks != test['expectedSA'] or lcpFromEncoded != lcp or plcp != test['expectedPCLP']:
            print("SA ", sa.ranks, "expect: ", test['expectedSA'])
            print("LCP ", lcpFromEncoded, "expect: ", lcp)
            print("PLCP ", plcp, "expect: ", test['expectedPCLP'])
            print(" ")


            failed += 1
        else:
            passed += 1
    print(f'PASSED = {passed}, FAILED = {failed}')