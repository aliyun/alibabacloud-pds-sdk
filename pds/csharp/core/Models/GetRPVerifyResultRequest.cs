// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 
     */
    public class GetRPVerifyResultRequest : TeaModel {
        /// <summary>
        /// During Verify Process, 是否在实人认证流程中调用
        /// </summary>
        [NameInMap("during_verify_process")]
        [Validation(Required=false)]
        public bool? DuringVerifyProcess { get; set; }

        /// <summary>
        /// User ID, 当前访问的用户
        /// </summary>
        [NameInMap("user_id")]
        [Validation(Required=true)]
        public string UserId { get; set; }

    }

}
