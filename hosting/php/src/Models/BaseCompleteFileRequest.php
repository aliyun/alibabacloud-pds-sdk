<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\Hosting\SDK\Models;

use AlibabaCloud\Tea\Model;

use Aliyun\Hosting\SDK\Models\UploadPartInfo;

/**
 * complete file request
 */
class BaseCompleteFileRequest extends Model {
    protected $_name = [
        'additionData' => 'addition_data',
        'driveId' => 'drive_id',
        'partInfoList' => 'part_info_list',
        'shareId' => 'share_id',
        'uploadId' => 'upload_id',
    ];
    public function validate() {
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
    }
    public function toMap() {
        $res = [];
        if (null !== $this->additionData) {
            $res['addition_data'] = $this->additionData;
        }
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->partInfoList) {
            $res['part_info_list'] = [];
            if(null !== $this->partInfoList && is_array($this->partInfoList)){
                $n = 0;
                foreach($this->partInfoList as $item){
                    $res['part_info_list'][$n++] = null !== $item ? $item->toMap() : $item;
                }
            }
        }
        if (null !== $this->shareId) {
            $res['share_id'] = $this->shareId;
        }
        if (null !== $this->uploadId) {
            $res['upload_id'] = $this->uploadId;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return BaseCompleteFileRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['addition_data'])){
            $model->additionData = $map['addition_data'];
        }
        if(isset($map['drive_id'])){
            $model->driveId = $map['drive_id'];
        }
        if(isset($map['part_info_list'])){
            if(!empty($map['part_info_list'])){
                $model->partInfoList = [];
                $n = 0;
                foreach($map['part_info_list'] as $item) {
                    $model->partInfoList[$n++] = null !== $item ? UploadPartInfo::fromMap($item) : $item;
                }
            }
        }
        if(isset($map['share_id'])){
            $model->shareId = $map['share_id'];
        }
        if(isset($map['upload_id'])){
            $model->uploadId = $map['upload_id'];
        }
        return $model;
    }
    /**
     * @description addition_data
     * @var mixed[]
     */
    public $additionData;

    /**
     * @description drive_id
     * @example 1
     * @var string
     */
    public $driveId;

    /**
     * @description part_info_list
     * @var UploadPartInfo[]
     */
    public $partInfoList;

    /**
     * @var string
     */
    public $shareId;

    /**
     * @description upload_id
     * @var string
     */
    public $uploadId;

}
