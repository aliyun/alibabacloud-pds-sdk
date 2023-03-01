// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class CheckExistResponse extends TeaModel {
    /**
     * <p>当前手机号是否存在</p>
     */
    @NameInMap("is_exist")
    @Validation(required = true)
    public Boolean isExist;

    /**
     * <p>待查询的手机号</p>
     */
    @NameInMap("phone_number")
    @Validation(required = true)
    public String phoneNumber;

    /**
     * <p>国家编号，默认86，不需要填+号，直接填数字</p>
     */
    @NameInMap("phone_region")
    public String phoneRegion;

    public static CheckExistResponse build(java.util.Map<String, ?> map) throws Exception {
        CheckExistResponse self = new CheckExistResponse();
        return TeaModel.build(map, self);
    }

    public CheckExistResponse setIsExist(Boolean isExist) {
        this.isExist = isExist;
        return this;
    }
    public Boolean getIsExist() {
        return this.isExist;
    }

    public CheckExistResponse setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
        return this;
    }
    public String getPhoneNumber() {
        return this.phoneNumber;
    }

    public CheckExistResponse setPhoneRegion(String phoneRegion) {
        this.phoneRegion = phoneRegion;
        return this;
    }
    public String getPhoneRegion() {
        return this.phoneRegion;
    }

}
