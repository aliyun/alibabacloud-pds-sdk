// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * Pre hash check Response
 */
public class PreHashCheckSuccessResponse extends TeaModel {
    // code
    @NameInMap("code")
    public String code;

    // file_name
    @NameInMap("file_name")
    public String fileName;

    // message
    @NameInMap("message")
    public String message;

    // parent_file_id
    @NameInMap("parent_file_id")
    @Validation(required = true, pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String parentFileId;

    // pre_hash
    @NameInMap("pre_hash")
    public String preHash;

    public static PreHashCheckSuccessResponse build(java.util.Map<String, ?> map) throws Exception {
        PreHashCheckSuccessResponse self = new PreHashCheckSuccessResponse();
        return TeaModel.build(map, self);
    }

    public PreHashCheckSuccessResponse setCode(String code) {
        this.code = code;
        return this;
    }
    public String getCode() {
        return this.code;
    }

    public PreHashCheckSuccessResponse setFileName(String fileName) {
        this.fileName = fileName;
        return this;
    }
    public String getFileName() {
        return this.fileName;
    }

    public PreHashCheckSuccessResponse setMessage(String message) {
        this.message = message;
        return this;
    }
    public String getMessage() {
        return this.message;
    }

    public PreHashCheckSuccessResponse setParentFileId(String parentFileId) {
        this.parentFileId = parentFileId;
        return this;
    }
    public String getParentFileId() {
        return this.parentFileId;
    }

    public PreHashCheckSuccessResponse setPreHash(String preHash) {
        this.preHash = preHash;
        return this;
    }
    public String getPreHash() {
        return this.preHash;
    }

}
