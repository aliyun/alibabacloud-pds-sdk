<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * Remove story images response.
 */
class RemoveStoryImagesResponse extends Model
{
    /**
     * @description drive_id
     *
     * @var string
     */
    public $driveId;

    /**
     * @description file_ids
     *
     * @example a, b, c
     *
     * @var string[]
     */
    public $fileIds;

    /**
     * @var RemoveStoryImagesResultItem[]
     */
    public $results;

    /**
     * @description story_id
     *
     * @var string
     */
    public $storyId;

    /**
     * @description success_file_ids
     *
     * @var string[]
     */
    public $successFileIds;
    protected $_name = [
        'driveId'        => 'drive_id',
        'fileIds'        => 'file_ids',
        'results'        => 'results',
        'storyId'        => 'story_id',
        'successFileIds' => 'success_file_ids',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->fileIds) {
            $res['file_ids'] = $this->fileIds;
        }
        if (null !== $this->results) {
            $res['results'] = [];
            if (null !== $this->results && \is_array($this->results)) {
                $n = 0;
                foreach ($this->results as $item) {
                    $res['results'][$n++] = null !== $item ? $item->toMap() : $item;
                }
            }
        }
        if (null !== $this->storyId) {
            $res['story_id'] = $this->storyId;
        }
        if (null !== $this->successFileIds) {
            $res['success_file_ids'] = $this->successFileIds;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return RemoveStoryImagesResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['drive_id'])) {
            $model->driveId = $map['drive_id'];
        }
        if (isset($map['file_ids'])) {
            if (!empty($map['file_ids'])) {
                $model->fileIds = $map['file_ids'];
            }
        }
        if (isset($map['results'])) {
            if (!empty($map['results'])) {
                $model->results = [];
                $n              = 0;
                foreach ($map['results'] as $item) {
                    $model->results[$n++] = null !== $item ? RemoveStoryImagesResultItem::fromMap($item) : $item;
                }
            }
        }
        if (isset($map['story_id'])) {
            $model->storyId = $map['story_id'];
        }
        if (isset($map['success_file_ids'])) {
            if (!empty($map['success_file_ids'])) {
                $model->successFileIds = $map['success_file_ids'];
            }
        }

        return $model;
    }
}
