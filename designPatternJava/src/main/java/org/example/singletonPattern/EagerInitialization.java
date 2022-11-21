package org.example.singletonPattern;

public class EagerInitialization {
    private static final EagerInitialization instance = new EagerInitialization();

    // 构造函数私有化, 只能在本类中调用，本类外调用将报错
    private EagerInitialization() {
    }

    // 获取实例的接口
    public static EagerInitialization getInstance() {
        return instance;
    }
}

