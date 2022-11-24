package org.example.singletonPattern;

public class SafeLazyInitialization {
    private static SafeLazyInitialization instance;

    private SafeLazyInitialization() {
    }

    public static SafeLazyInitialization getInstance() {
        if (instance == null) {
            synchronized (SafeLazyInitialization.class) {
                if (instance == null) {
                    instance = new SafeLazyInitialization();
                }
            }
        }
        return instance;
    }


}
