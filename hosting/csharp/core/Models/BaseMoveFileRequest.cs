// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 文件移动请求
     */
    public class BaseMoveFileRequest : TeaModel {
        /// <summary>
        /// drive_id
        /// </summary>
        [NameInMap("drive_id")]
        [Validation(Required=true, Pattern="[0-9]+")]
        public string DriveId { get; set; }

        /// <summary>
        /// new_name
        /// </summary>
        [NameInMap("new_name")]
        [Validation(Required=false, MaxLength=1024)]
        public string NewName { get; set; }

        [NameInMap("share_id")]
        [Validation(Required=false)]
        public string ShareId { get; set; }

    }

}
