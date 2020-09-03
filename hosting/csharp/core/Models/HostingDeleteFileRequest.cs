// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 删除文件请求
     */
    public class HostingDeleteFileRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// drive_id
        /// </summary>
        [NameInMap("drive_id")]
        [Validation(Required=false, Pattern="[0-9]+")]
        public string DriveId { get; set; }

        /// <summary>
        /// file_path
        /// </summary>
        [NameInMap("file_path")]
        [Validation(Required=true, MaxLength=1000)]
        public string FilePath { get; set; }

        /// <summary>
        /// permanently
        /// type: false
        /// </summary>
        [NameInMap("permanently")]
        [Validation(Required=false)]
        public bool? Permanently { get; set; }

        /// <summary>
        /// share_id
        /// </summary>
        [NameInMap("share_id")]
        [Validation(Required=false, Pattern="[0-9a-zA-Z-]+")]
        public string ShareId { get; set; }

    }

}
