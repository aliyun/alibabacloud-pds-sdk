// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class GetAppDebugCmdResponse extends TeaModel {
    // cmd
    @NameInMap("cmd")
    public String cmd;

    public static GetAppDebugCmdResponse build(java.util.Map<String, ?> map) throws Exception {
        GetAppDebugCmdResponse self = new GetAppDebugCmdResponse();
        return TeaModel.build(map, self);
    }

    public GetAppDebugCmdResponse setCmd(String cmd) {
        this.cmd = cmd;
        return this;
    }
    public String getCmd() {
        return this.cmd;
    }

}
