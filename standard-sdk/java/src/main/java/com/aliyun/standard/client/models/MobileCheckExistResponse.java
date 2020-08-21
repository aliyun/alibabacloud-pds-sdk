// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class MobileCheckExistResponse extends TeaModel {
    // 当前手机号是否存在
    @NameInMap("is_exist")
    @Validation(required = true)
    public Boolean isExist;

    // 待查询的手机号
    @NameInMap("phone_number")
    @Validation(required = true)
    public String phoneNumber;

    // 国家编号，默认86，不需要填+号，直接填数字
    @NameInMap("phone_region")
    public String phoneRegion;

    public static MobileCheckExistResponse build(java.util.Map<String, ?> map) throws Exception {
        MobileCheckExistResponse self = new MobileCheckExistResponse();
        return TeaModel.build(map, self);
    }

    public MobileCheckExistResponse setIsExist(Boolean isExist) {
        this.isExist = isExist;
        return this;
    }
    public Boolean getIsExist() {
        return this.isExist;
    }

    public MobileCheckExistResponse setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
        return this;
    }
    public String getPhoneNumber() {
        return this.phoneNumber;
    }

    public MobileCheckExistResponse setPhoneRegion(String phoneRegion) {
        this.phoneRegion = phoneRegion;
        return this;
    }
    public String getPhoneRegion() {
        return this.phoneRegion;
    }

}
