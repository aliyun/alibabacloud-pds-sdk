// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class RemoveStoryImagesResultItem extends TeaModel {
    // code
    @NameInMap("code")
    public String code;

    // file_id
    @NameInMap("file_id")
    public String fileId;

    // is_succeed
    @NameInMap("is_succeed")
    public Boolean isSucceed;

    // message
    @NameInMap("message")
    public String message;

    public static RemoveStoryImagesResultItem build(java.util.Map<String, ?> map) throws Exception {
        RemoveStoryImagesResultItem self = new RemoveStoryImagesResultItem();
        return TeaModel.build(map, self);
    }

    public RemoveStoryImagesResultItem setCode(String code) {
        this.code = code;
        return this;
    }
    public String getCode() {
        return this.code;
    }

    public RemoveStoryImagesResultItem setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public RemoveStoryImagesResultItem setIsSucceed(Boolean isSucceed) {
        this.isSucceed = isSucceed;
        return this;
    }
    public Boolean getIsSucceed() {
        return this.isSucceed;
    }

    public RemoveStoryImagesResultItem setMessage(String message) {
        this.message = message;
        return this;
    }
    public String getMessage() {
        return this.message;
    }

}
