// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 文件拷贝 response
     */
    public class HostingCopyFileResponse : TeaModel {
        /// <summary>
        /// async_task_id
        /// </summary>
        [NameInMap("async_task_id")]
        [Validation(Required=false)]
        public string AsyncTaskId { get; set; }

        /// <summary>
        /// domain_id
        /// </summary>
        [NameInMap("domain_id")]
        [Validation(Required=false, Pattern="[a-z0-9A-Z-]+")]
        public string DomainId { get; set; }

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
        [Validation(Required=false)]
        public string FilePath { get; set; }

        /// <summary>
        /// drive_id
        /// </summary>
        [NameInMap("share_id")]
        [Validation(Required=false, Pattern="[a-z0-9A-Z]+")]
        public string ShareId { get; set; }

    }

}
